# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class MgmtMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mgmt_interface(self: SharedUtils) -> str | None:
        """
        mgmt_interface is inherited from
        Global var mgmt_interface ->
          Platform Settings management_interface ->
            Fabric Topology data model mgmt_interface
        """
        return default(
            get(self.switch_data_combined, "mgmt_interface"),
            self.platform_settings.get("management_interface"),
            get(self.hostvars, "mgmt_interface"),
            get(self.cv_topology_config, "mgmt_interface"),
            "Management1",
        )

    @cached_property
    def ipv6_mgmt_ip(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "ipv6_mgmt_ip")

    @cached_property
    def mgmt_ip(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "mgmt_ip")

    @cached_property
    def mgmt_interface_vrf(self: SharedUtils) -> str:
        return get(self.hostvars, "mgmt_interface_vrf", default="MGMT")

    @cached_property
    def mgmt_gateway(self: SharedUtils) -> str | None:
        return get(self.hostvars, "mgmt_gateway")

    @cached_property
    def ipv6_mgmt_gateway(self: SharedUtils) -> str | None:
        return get(self.hostvars, "ipv6_mgmt_gateway")

    @cached_property
    def default_mgmt_method(self: SharedUtils) -> str | None:
        """
        This is only executed if some protocol looks for the default value, so we can raise here to ensure a working config.

        The check for 'inband_mgmt_interface' relies on other indirect checks done in that code.
        """
        default_mgmt_method = get(self.hostvars, "default_mgmt_method", default="oob")
        if default_mgmt_method == "oob":
            if (self.mgmt_ip is None) and (self.ipv6_mgmt_ip is None):
                raise AristaAvdMissingVariableError("'default_mgmt_method: oob' requires either 'mgmt_ip' or 'ipv6_mgmt_ip' to bet set.")

            return default_mgmt_method

        elif default_mgmt_method == "inband":
            # Check for missing interface
            if self.inband_mgmt_interface is None:
                raise AristaAvdMissingVariableError("'default_mgmt_method: inband' requires 'inband_mgmt_interface' to be set.")

            return default_mgmt_method

        return None

    @cached_property
    def default_mgmt_protocol_vrf(self: SharedUtils) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.mgmt_interface_vrf
        elif self.default_mgmt_method == "inband":
            # inband_mgmt_vrf returns None for vrf default.
            return self.inband_mgmt_vrf or "default"

        return None

    @cached_property
    def default_mgmt_protocol_interface(self: SharedUtils) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.mgmt_interface
        elif self.default_mgmt_method == "inband":
            return self.inband_mgmt_interface

        return None
