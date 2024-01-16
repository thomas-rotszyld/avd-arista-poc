# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, load_python_class
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import AvdIpAddressing

if TYPE_CHECKING:
    from .shared_utils import SharedUtils

DEFAULT_AVD_IP_ADDRESSING_PYTHON_CLASS_NAME = "AvdIpAddressing"


class IpAddressingMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def loopback_ipv4_offset(self: SharedUtils) -> int:
        return get(self.switch_data_combined, "loopback_ipv4_offset", default=0)

    @cached_property
    def loopback_ipv6_offset(self: SharedUtils) -> int:
        return get(self.switch_data_combined, "loopback_ipv6_offset", default=0)

    @cached_property
    def loopback_ipv6_pool(self: SharedUtils) -> str:
        return get(self.switch_data_combined, "loopback_ipv6_pool", required=True)

    @cached_property
    def uplink_ipv4_pool(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "uplink_ipv4_pool")

    @cached_property
    def loopback_ipv4_pool(self: SharedUtils) -> str:
        return get(self.switch_data_combined, "loopback_ipv4_pool", required=True)

    @cached_property
    def vtep_loopback_ipv4_pool(self: SharedUtils) -> str:
        return get(self.switch_data_combined, "vtep_loopback_ipv4_pool", required=True)

    @cached_property
    def vtep_ip(self: SharedUtils) -> str:
        """
        Render ipv4 address for vtep_ip using dynamically loaded python module.
        """
        if self.mlag is True:
            return self.ip_addressing.vtep_ip_mlag()

        else:
            return self.ip_addressing.vtep_ip()

    @cached_property
    def vtep_vvtep_ip(self: SharedUtils) -> str | None:
        return get(self.hostvars, "vtep_vvtep_ip")

    @cached_property
    def ip_addressing(self: SharedUtils) -> AvdIpAddressing:
        """
        Load the python_module defined in `templates.ip_addressing.python_module`
        Return an instance of the class defined by `templates.ip_addressing.python_class_name` as cached_property
        """
        module_path = self.ip_addressing_templates.get("python_module")
        if module_path is None:
            return AvdIpAddressing(hostvars=self.hostvars, shared_utils=self)

        class_name = self.ip_addressing_templates.get("python_class_name", DEFAULT_AVD_IP_ADDRESSING_PYTHON_CLASS_NAME)

        cls = load_python_class(
            module_path,
            class_name,
            AvdIpAddressing,
        )

        return cls(hostvars=self.hostvars, shared_utils=self)

    @cached_property
    def ip_addressing_templates(self: SharedUtils) -> dict:
        """
        Return dict with ip_addressing templates set based on
        templates.ip_addressing.* combined with (overridden by)
        node_type_keys.<node_type_key>.ip_addressing.*
        """
        hostvar_templates = get(self.hostvars, "templates.ip_addressing", default={})
        node_type_templates = get(self.node_type_key_data, "ip_addressing", default={})
        if hostvar_templates or node_type_templates:
            return merge(hostvar_templates, node_type_templates, list_merge="replace", destructive_merge=False)
        else:
            return {}
