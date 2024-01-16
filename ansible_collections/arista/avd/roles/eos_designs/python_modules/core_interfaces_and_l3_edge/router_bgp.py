# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError

from .utils import UtilsMixin


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        Return structured config for router_bgp
        """

        if not self.shared_utils.underlay_bgp:
            return None

        neighbors = []
        neighbor_interfaces = []
        for p2p_link in self._filtered_p2p_links:
            if not (p2p_link.get("include_in_underlay_protocol", True) is True):
                continue

            if p2p_link["data"]["bgp_as"] is None or p2p_link["data"]["peer_bgp_as"] is None:
                raise AristaAvdMissingVariableError("l3_edge.p2p_links.[].as")

            neighbor = {
                "remote_as": p2p_link["data"]["peer_bgp_as"],
                "peer": p2p_link["data"]["peer"],
                "description": p2p_link["data"]["peer"],
                "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
            }

            # RFC5549
            if self.shared_utils.underlay_rfc5549:
                neighbor_interfaces.append({"name": p2p_link["data"]["interface"], **neighbor})
                continue

            # Regular BGP Neighbors
            if p2p_link["data"]["ip"] is None or p2p_link["data"]["peer_ip"] is None:
                raise AristaAvdMissingVariableError("l3_edge.p2p_links.[].ip, .subnet or .ip_pool")

            neighbor["bfd"] = p2p_link.get("bfd")
            if p2p_link["data"]["bgp_as"] != self.shared_utils.bgp_as:
                neighbor["local_as"] = p2p_link["data"]["bgp_as"]

            # Remove None values
            neighbor = {key: value for key, value in neighbor.items() if value is not None}

            neighbors.append({"ip_address": p2p_link["data"]["peer_ip"].split("/")[0], **neighbor})

        router_bgp = {}
        if neighbors:
            router_bgp["neighbors"] = neighbors

        if neighbor_interfaces:
            router_bgp["neighbor_interfaces"] = neighbor_interfaces

        if router_bgp:
            return router_bgp

        return None
