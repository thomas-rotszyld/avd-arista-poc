# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, default, get

from .utils import UtilsMixin


class StandardAccessListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def standard_access_lists(self) -> list | None:
        """
        return structured config for standard_access_lists

        Used for to configure ACLs used by multicast RPs in each VRF
        """

        if not self.shared_utils.network_services_l3:
            return None

        standard_access_lists = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for rp_entry in default(get(vrf, "pim_rp_addresses"), get(tenant, "pim_rp_addresses"), []):
                    if self.shared_utils.hostname in get(rp_entry, "nodes", default=[self.shared_utils.hostname]):
                        if rp_entry.get("groups") is None or rp_entry.get("access_list_name") is None:
                            continue

                        standard_access_list = {
                            "name": rp_entry["access_list_name"],
                            "sequence_numbers": [
                                {
                                    "sequence": (index + 1) * 10,
                                    "action": f"permit {group}",
                                }
                                for index, group in enumerate(rp_entry["groups"])
                            ],
                        }

                        append_if_not_duplicate(
                            list_of_dicts=standard_access_lists,
                            primary_key="name",
                            new_dict=standard_access_list,
                            context="PIM RP Address ACL for VRFs",
                            context_keys=["name"],
                        )

        if standard_access_lists:
            return standard_access_lists

        return None
