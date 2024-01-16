# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Generator

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AvdConversionWarning, AvdDeprecationWarning
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_all

SCHEMA_TO_PY_TYPE_MAP = {
    "str": str,
    "int": int,
    "bool": bool,
    "float": float,
    "dict": dict,
    "list": list,
}
SIMPLE_CONVERTERS = {
    "str": str,
    "int": int,
    "bool": bool,
}


class AvdDataConverter:
    """
    AvdDataConverter is used to convert AVD Data Types based on schema options.

    avdschema argument is an instance of AvdSchema. Type hinting is not working because of circular import
    TODO: Refactor to take a fully resolved schema as dict
    """

    def __init__(self, avdschema):
        self._avdschema = avdschema

        # We run through all the regular keys first, to ensure that all data has been converted
        # in case some of it is referenced in "dynamic_keys" below
        self.converters = {
            "items": self.convert_items,
            "keys": self.convert_keys,
            "dynamic_keys": self.convert_dynamic_keys,
            "deprecation": self.deprecation,
        }

    def convert_data(self, data, schema: dict = None, path: list[str] = None) -> Generator:
        """
        Perform in-place conversion of data according to the provided schema.
        Main entry function which is recursively called from the child functions performing the actual conversion of keys/items.
        """
        if schema is None:
            # Get fully resolved schema (where all $ref has been expanded recursively)
            schema = self._avdschema.resolved_schema

        if path is None:
            path = []

        for key, converter in self.converters.items():
            if key not in schema:
                # Ignore keys not in schema
                continue

            # Converters will do inplace update of data. Any returns will be yielded conversion messages.
            yield from converter(schema[key], data, schema, path)

    def convert_keys(self, keys: dict, data: dict, schema: dict, path: list[str]):
        """
        This function performs conversion on each key with the relevant subschema
        """
        if not isinstance(data, dict):
            return

        for key, childschema in keys.items():
            if key not in data:
                # Skip key since there is nothing to convert if the key is not set in data
                continue

            # Perform type conversion of the data for the child key if required based on "convert_types"
            if "convert_types" in childschema:
                yield from self.convert_types(childschema["convert_types"], data, key, childschema, path + [key])

            # Convert to lower case if set in schema and value is a string
            if childschema.get("convert_to_lower_case") and isinstance(data[key], str):
                data[key] = data[key].lower()

            yield from self.convert_data(data[key], childschema, path + [key])

    def convert_dynamic_keys(self, dynamic_keys: dict, data: dict, schema: dict, path: list[str]):
        """
        This function resolves "dynamic_keys" by looking in the actual data.
        Then calls convert_keys to performs conversion on each resolved key with the relevant subschema
        """
        if not isinstance(data, dict):
            return

        # Resolve "keys" from schema "dynamic_keys" by looking for the dynamic key in data.
        keys = {}
        for dynamic_key, childschema in dynamic_keys.items():
            resolved_keys = get_all(data, dynamic_key)
            for resolved_key in resolved_keys:
                keys.setdefault(resolved_key, childschema)

        # Reuse convert_keys to perform the actual conversion on the resolved dynamic keys
        yield from self.convert_keys(keys, data, schema, path)

    def convert_items(self, items: dict, data: list, schema: dict, path: list[str]):
        """
        This function performs conversion on each item with the items subschema
        """
        if not isinstance(data, list):
            return

        for index, item in enumerate(data):
            # Perform type conversion of the items data if required based on "convert_types"
            if "convert_types" in items:
                yield from self.convert_types(items["convert_types"], data, index, items, path + [index])

            # Convert to lower case if set in schema and item is a string
            if items.get("convert_to_lower_case") and isinstance(item, str):
                data[index] = item.lower()

            # Dive in to child items/schema
            yield from self.convert_data(item, items, path + [index])

    def convert_types(self, convert_types: list, data: dict | list, index: str | int, schema: dict, path: list[str]):
        """
        This function performs type conversion if necessary on a single data instance.
        It is invoked for child keys during "keys" conversion and for child items during
        "items" conversion

        "data" is either the parent dict or the parent list.
        "index" is either the key of the parent dict or the index of the parent list.

        Conversion is performed in-place using the provided "data" and "index"

        Yields AvdConversionWarning and/or AvdDeprecationWarning except for simple str/int/bool conversions

        Any conversion errors are ignored and the original value is returned
        """
        schema_type = schema.get("type")

        # Get value from input data
        value = data[index]

        # For simple conversions, skip conversion if the value is of the correct type
        if schema_type in SIMPLE_CONVERTERS and isinstance(value, SCHEMA_TO_PY_TYPE_MAP.get(schema_type)):
            # Avoid corner case where we want to convert bool to int. Bool is a subclass of Int so it passes the check above.
            if not (schema_type == "int" and isinstance(value, bool)):
                return

        for convert_type in convert_types:
            if isinstance(value, SCHEMA_TO_PY_TYPE_MAP.get(convert_type)):
                if schema_type in SIMPLE_CONVERTERS:
                    try:
                        data[index] = SIMPLE_CONVERTERS[schema_type](value)
                    except Exception:
                        # Ignore errors
                        # TODO: Log message
                        return

                    # Here we do not yield an AvdConversionWarning, since these will be accepted going forward.

                elif convert_type in ["dict", "list"] and schema_type == "list" and "primary_key" in schema:
                    try:
                        data[index] = convert_dicts(value, schema["primary_key"], secondary_key=schema.get("secondary_key"))
                    except Exception:
                        # Ignore errors
                        # TODO: Log message
                        return

                    if data[index] == value:
                        # No change - when input is list and have the correct format in all items
                        return

                    yield AvdConversionWarning(key=path, oldtype=convert_type, newtype=schema_type)

                elif convert_type == "dict" and schema_type == "list":
                    try:
                        data[index] = list(value)
                    except Exception:
                        # Ignore errors
                        # TODO: Log message
                        return

                    yield AvdConversionWarning(key=path, oldtype=convert_type, newtype=schema_type)

                elif convert_type == "str" and schema_type == "list":
                    try:
                        data[index] = list(map(str.strip, value.split(",")))
                    except Exception:
                        # Ignore errors
                        # TODO: Log message
                        return

                    yield AvdConversionWarning(key=path, oldtype=convert_type, newtype=schema_type)

    def deprecation(self, deprecation: dict, data, schema: dict, path: list):
        """
        deprecation:
          warning: bool, default = True
          new_key: str
          removed: bool
          remove_in_version: str
          remove_after_date: str
          url: str
        """

        if not deprecation.get("warning", True):
            return

        yield AvdDeprecationWarning(
            key=path,
            new_key=deprecation.get("new_key"),
            remove_in_version=deprecation.get("remove_in_version"),
            remove_after_date=deprecation.get("remove_after_date"),
            url=deprecation.get("url"),
            removed=deprecation.get("removed", False),
        )
