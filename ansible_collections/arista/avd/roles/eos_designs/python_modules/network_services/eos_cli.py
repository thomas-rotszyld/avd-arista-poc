# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class EosCliMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def eos_cli(self) -> dict | None:
        """
        Return existing eos_cli plus any eos_cli from VRFs
        """

        if not self.shared_utils.network_services_l3:
            return None

        eos_clis = []
        if (eos_cli := get(self._hostvars, "eos_cli")) is not None:
            eos_clis.append(eos_cli)

        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if (eos_cli := vrf.get("raw_eos_cli")) is not None:
                    eos_clis.append(eos_cli)

        if eos_clis:
            return "\n".join(eos_clis)

        return None
