# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts

from .ethernet_interfaces import EthernetInterfacesMixin
from .monitor_sessions import MonitorSessionsMixin
from .port_channel_interfaces import PortChannelInterfacesMixin


class AvdStructuredConfigConnectedEndpoints(
    AvdFacts,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    MonitorSessionsMixin,
):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more managable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def render(self) -> dict:
        """
        Wrap class render function with a check if connected_endpoints feature is enabled
        """
        if self.shared_utils.connected_endpoints:
            return super().render()
        return {}
