# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class CvTopology:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def cv_topology(self: SharedUtils) -> dict | None:
        """
        Returns the cv_topology for this device like
        {
            hostname: <str>,
            platform: <str | None>,
            interfaces: [
                {
                    name: <str>
                    neighbor: <str>
                    neighbor_interface: <str>
                }
            ]

        """
        if get(self.hostvars, "use_cv_topology") is not True:
            return None

        cv_topology = get(
            self.hostvars,
            "cv_topology",
            required=True,
            org_key="Found 'use_cv_topology:true' so 'cv_topology'",
        )

        return get_item(cv_topology, "hostname", self.hostname)

    @cached_property
    def cv_topology_platform(self: SharedUtils) -> str | None:
        if self.cv_topology is not None:
            return self.cv_topology.get("platform")

    @cached_property
    def cv_topology_config(self: SharedUtils) -> dict:
        """
        Returns dict with keys derived from cv topology (or empty dict)
        {
            uplink_interfaces: <list>
            uplink_switches: <list>
            uplink_switch_interfaces: <list>
            mlag_interfaces: <list>
            mlag_peer: <str>
            mgmt_interface: <str>
        }
        """
        if self.cv_topology is None:
            return {}

        cv_interfaces = get(self.cv_topology, "interfaces", default=[])
        default_uplink_interfaces = range_expand(
            get(
                self.default_interfaces,
                "uplink_interfaces",
                required=True,
                org_key="Found 'use_cv_topology:true' so 'default_interfaces.[].uplink_interfaces'",
            )
        )
        config = {}
        for uplink_interface in default_uplink_interfaces:
            if cv_interface := get_item(cv_interfaces, "name", uplink_interface):
                config.setdefault("uplink_interfaces", []).append(cv_interface["name"])
                config.setdefault("uplink_switches", []).append(cv_interface["neighbor"])
                config.setdefault("uplink_switch_interfaces", []).append(cv_interface["neighbor_interface"])

        if not self.mlag:
            return config

        default_mlag_interfaces = range_expand(
            get(
                self.default_interfaces,
                "mlag_interfaces",
                required=True,
                org_key="Found 'use_cv_topology:true' so 'default_interfaces.[].mlag_interfaces'",
            )
        )
        for mlag_interface in default_mlag_interfaces:
            if cv_interface := get_item(cv_interfaces, "name", mlag_interface):
                config.setdefault("mlag_interfaces", []).append(cv_interface["name"])
                # TODO: Set mlag_peer once we get a user-defined var for that.
                # config["mlag_peer"] = cv_interface["neighbor"]

        for cv_interface in cv_interfaces:
            if cv_interface["name"].startswith("Management"):
                config["mgmt_interface"] = cv_interface["name"]

        return config
