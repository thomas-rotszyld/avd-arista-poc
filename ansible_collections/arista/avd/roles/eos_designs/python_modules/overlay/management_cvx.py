# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class ManagementCvxMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def management_cvx(self) -> dict | None:
        if not (self.shared_utils.overlay_cvx and self.shared_utils.overlay_vtep):
            return None

        server_hosts = []
        overlay_cvx_servers = get(self._hostvars, "overlay_cvx_servers", required=True)
        for overlay_cvx_server in overlay_cvx_servers:
            peer_switch_facts = self.shared_utils.get_peer_facts(overlay_cvx_server, required=True)
            cvx_server_ip = get(peer_switch_facts, "mgmt_ip", required=True, org_key=f"'mgmt_ip' for CVX Server {overlay_cvx_server}")
            server_hosts.append(str(ip_interface(cvx_server_ip).ip))

        return {
            "shutdown": False,
            "source_interface": "Loopback0",
            "server_hosts": server_hosts,
        }
