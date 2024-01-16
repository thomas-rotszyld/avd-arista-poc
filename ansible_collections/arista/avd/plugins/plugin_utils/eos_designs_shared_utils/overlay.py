# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_address
from re import fullmatch
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class OverlayMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def vtep_loopback(self: SharedUtils) -> str:
        return get(self.switch_data_combined, "vtep_loopback", default="Loopback1")

    @cached_property
    def evpn_role(self: SharedUtils) -> str | None:
        if self.underlay_router is True:
            default_evpn_role = get(self.node_type_key_data, "default_evpn_role", default="none")
            return get(self.switch_data_combined, "evpn_role", default=default_evpn_role)
        return None

    @cached_property
    def mpls_overlay_role(self: SharedUtils) -> str | None:
        if self.underlay_router is True:
            default_mpls_overlay_role = get(self.node_type_key_data, "default_mpls_overlay_role", default="none")
            return get(self.switch_data_combined, "mpls_overlay_role", default=default_mpls_overlay_role)
        return None

    @cached_property
    def overlay_rd_type(self: SharedUtils) -> dict:
        overlay_rd_type = get(self.hostvars, "overlay_rd_type", default={})
        admin_subfield = get(overlay_rd_type, "admin_subfield", default="overlay_loopback_ip")
        admin_subfield_offset = int(get(overlay_rd_type, "admin_subfield_offset", default=0))
        return {
            "admin_subfield": admin_subfield,
            "admin_subfield_offset": admin_subfield_offset,
            "vrf_admin_subfield": get(overlay_rd_type, "vrf_admin_subfield", default=admin_subfield),
            "vrf_admin_subfield_offset": int(get(overlay_rd_type, "vrf_admin_subfield_offset", default=admin_subfield_offset)),
            "vlan_assigned_number_subfield": get(overlay_rd_type, "vlan_assigned_number_subfield", default="mac_vrf_id"),
        }

    @cached_property
    def overlay_rt_type(self: SharedUtils) -> dict:
        overlay_rt_type = get(self.hostvars, "overlay_rt_type", default={})
        admin_subfield = get(overlay_rt_type, "admin_subfield", default="vrf_id")
        return {
            "admin_subfield": admin_subfield,
            "vrf_admin_subfield": get(overlay_rt_type, "vrf_admin_subfield", default=admin_subfield),
            "vlan_assigned_number_subfield": get(overlay_rt_type, "vlan_assigned_number_subfield", default="mac_vrf_id"),
        }

    @cached_property
    def overlay_rd_type_admin_subfield(self: SharedUtils) -> str:
        admin_subfield = self.overlay_rd_type["admin_subfield"]
        admin_subfield_offset = self.overlay_rd_type["admin_subfield_offset"]
        return self.get_rd_admin_subfield_value(admin_subfield, admin_subfield_offset)

    @cached_property
    def overlay_rd_type_vrf_admin_subfield(self: SharedUtils) -> str:
        vrf_admin_subfield = self.overlay_rd_type["vrf_admin_subfield"]
        vrf_admin_subfield_offset = self.overlay_rd_type["vrf_admin_subfield_offset"]
        return self.get_rd_admin_subfield_value(vrf_admin_subfield, vrf_admin_subfield_offset)

    def get_rd_admin_subfield_value(self: SharedUtils, admin_subfield, admin_subfield_offset):
        if admin_subfield == "overlay_loopback_ip":
            return self.router_id

        if admin_subfield == "vtep_loopback":
            return self.vtep_ip

        if admin_subfield == "bgp_as":
            return self.bgp_as

        if admin_subfield == "switch_id":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and 'overlay_rd_type_admin_subfield' is set to 'switch_id'")
            return self.id + admin_subfield_offset

        if fullmatch(r"[0-9]+", str(admin_subfield)):
            return str(int(admin_subfield) + admin_subfield_offset)

        try:
            ip_address(admin_subfield)
            return admin_subfield
        except ValueError:
            pass

        return self.router_id

    @cached_property
    def evpn_gateway_vxlan_l2(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "evpn_gateway.evpn_l2.enabled", default=False)

    @cached_property
    def evpn_gateway_vxlan_l3(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "evpn_gateway.evpn_l3.enabled", default=False)

    @cached_property
    def evpn_gateway_vxlan_l3_inter_domain(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "evpn_gateway.evpn_l3.inter_domain", default=True)

    @cached_property
    def overlay_routing_protocol_address_family(self: SharedUtils) -> str:
        overlay_routing_protocol_address_family = get(self.hostvars, "overlay_routing_protocol_address_family", default="ipv4")
        if overlay_routing_protocol_address_family == "ipv6":
            if not (self.underlay_ipv6 is True and self.underlay_rfc5549):
                raise AristaAvdError(
                    "'overlay_routing_protocol_address_family: ipv6' is only supported in combination with 'underlay_ipv6: True' and 'underlay_rfc5549: True'"
                )
        return overlay_routing_protocol_address_family

    @cached_property
    def evpn_encapsulation(self: SharedUtils) -> str:
        """
        EVPN encapsulation based on fabric_evpn_encapsulation and node default_evpn_encapsulation.
        """
        return get(self.hostvars, "fabric_evpn_encapsulation", default=get(self.node_type_key_data, "default_evpn_encapsulation", default="vxlan"))

    @cached_property
    def overlay_evpn(self: SharedUtils) -> bool:
        # Set overlay_evpn to enable EVPN on the node
        return (
            self.bgp
            and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
            and self.overlay_routing_protocol in ["ebgp", "ibgp"]
            and "evpn" in self.overlay_address_families
        )

    @cached_property
    def overlay_mpls(self: SharedUtils) -> bool:
        """
        Set overlay_mpls to enable MPLS as the primary overlay
        """
        return any([self.overlay_evpn_mpls, self.overlay_vpn_ipv4, self.overlay_vpn_ipv6]) and not self.overlay_evpn_vxlan

    @cached_property
    def overlay_ipvpn_gateway(self: SharedUtils) -> bool:
        # Set overlay_ipvpn_gateway to trigger ipvpn interworking configuration.
        return self.overlay_evpn and get(self.switch_data_combined, "ipvpn_gateway.enabled", default=False)

    @cached_property
    def overlay_ler(self: SharedUtils) -> bool:
        return self.underlay_mpls and (self.mpls_overlay_role in ["client", "server"] or self.evpn_role in ["client", "server"]) and (self.any_network_services)

    @cached_property
    def overlay_vtep(self: SharedUtils) -> bool:
        # Set overlay_vtep to enable VXLAN VTEP
        return (
            self.overlay_routing_protocol in ["ebgp", "ibgp", "her", "cvx"]
            and (self.network_services_l2 or self.network_services_l3)
            and self.underlay_router
            and self.uplink_type == "p2p"
            and self.vtep
        )

    @cached_property
    def overlay_vpn_ipv4(self: SharedUtils) -> bool:
        # Set overlay_vpn_ipv4 enable IP-VPN configuration on the node.
        if self.bgp is not True:
            return False

        return (self.overlay_routing_protocol == "ibgp" and "vpn-ipv4" in self.overlay_address_families) or (
            "vpn-ipv4" in get(self.switch_data_combined, "ipvpn_gateway.address_families", default=["vpn-ipv4"]) and self.overlay_ipvpn_gateway
        )

    @cached_property
    def overlay_vpn_ipv6(self: SharedUtils) -> bool:
        # Set overlay_vpn_ipv4 to enable IP-VPN configuration on the node.
        if self.bgp is not True:
            return False

        return (self.overlay_routing_protocol == "ibgp" and "vpn-ipv6" in self.overlay_address_families) or (
            "vpn-ipv6" in get(self.switch_data_combined, "ipvpn_gateway.address_families", default=["vpn-ipv4"]) and self.overlay_ipvpn_gateway
        )

    @cached_property
    def overlay_peering_address(self: SharedUtils) -> str | None:
        if not self.underlay_router:
            return None

        if self.overlay_routing_protocol_address_family == "ipv6":
            return self.ipv6_router_id

        return self.router_id

    @cached_property
    def overlay_cvx(self: SharedUtils) -> bool:
        return self.overlay_routing_protocol == "cvx"

    @cached_property
    def overlay_her(self: SharedUtils) -> bool:
        return self.overlay_routing_protocol == "her"

    @cached_property
    def overlay_dpath(self: SharedUtils) -> bool:
        # Set dpath based on ipvpn_gateway parameters
        return self.overlay_ipvpn_gateway and get(self.switch_data_combined, "ipvpn_gateway.enable_d_path", default=True)

    @cached_property
    def overlay_evpn_vxlan(self: SharedUtils) -> bool:
        return self.overlay_evpn and self.evpn_encapsulation == "vxlan"

    @cached_property
    def overlay_evpn_mpls(self: SharedUtils) -> bool:
        return self.overlay_evpn and self.evpn_encapsulation == "mpls"

    @cached_property
    def overlay_mlag_rfc5549(self: SharedUtils) -> bool:
        return get(self.hostvars, "overlay_mlag_rfc5549") is True
