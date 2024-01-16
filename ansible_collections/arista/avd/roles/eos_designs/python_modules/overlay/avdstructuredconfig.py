# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts

from .cvx import CvxMixin
from .ip_extcommunity_lists import IpExtCommunityListsMixin
from .management_cvx import ManagementCvxMixin
from .route_maps import RouteMapsMixin
from .router_bfd import RouterBfdMixin
from .router_bgp import RouterBgpMixin


class AvdStructuredConfigOverlay(
    AvdFacts,
    CvxMixin,
    IpExtCommunityListsMixin,
    ManagementCvxMixin,
    RouterBfdMixin,
    RouterBgpMixin,
    RouteMapsMixin,
):
    """
    The AvdStructuredConfig Class is imported used "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to get the render, keys and other attributes.
    All other methods are included as "Mixins" to make the files more managable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def render(self) -> dict:
        """
        Wrap class render function with a check if one of the following vars are True:
        - overlay_cvx
        - overlay_evpn
        - overlay_vpn_ipv4
        - overlay_vpn_ipv6
        """
        if any(
            [
                self.shared_utils.overlay_cvx,
                self.shared_utils.overlay_evpn,
                self.shared_utils.overlay_vpn_ipv4,
                self.shared_utils.overlay_vpn_ipv6,
            ]
        ):
            return super().render()
        return {}
