# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from hashlib import sha256
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .eos_designs_facts import EosDesignsFacts


class ShortEsiMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def _short_esi(self: EosDesignsFacts) -> str:
        """
        If short_esi is set to "auto" we will use sha256 to create a
        unique short_esi value based on various uplink information.
        """
        short_esi = get(self.shared_utils.switch_data_combined, "short_esi")
        if short_esi == "auto":
            esi_seed_1 = "".join(self.shared_utils.uplink_switches[:2])
            esi_seed_2 = "".join(self._uplink_switch_interfaces[:2])
            esi_seed_3 = "".join(default(self._uplink_interfaces, [])[:2])
            esi_seed_4 = default(self.shared_utils.group, "")
            esi_hash = sha256(f"{esi_seed_1}{esi_seed_2}{esi_seed_3}{esi_seed_4}".encode("UTF-8")).hexdigest()
            short_esi = re.sub(r"([0-9a-f]{4})", r"\1:", esi_hash)[:14]
        return short_esi
