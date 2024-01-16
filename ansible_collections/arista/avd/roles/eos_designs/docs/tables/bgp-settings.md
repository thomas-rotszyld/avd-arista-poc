<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  | AS number to use to configure overlay when "overlay_routing_protocol" == ibgp. |
    | [<samp>bgp_default_ipv4_unicast</samp>](## "bgp_default_ipv4_unicast") | Boolean |  | `False` |  | Default activation of IPv4 unicast address-family on all IPv4 neighbors.<br>It is best practice to disable activation.<br> |
    | [<samp>bgp_distance</samp>](## "bgp_distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;external_routes</samp>](## "bgp_distance.external_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;internal_routes</samp>](## "bgp_distance.internal_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;local_routes</samp>](## "bgp_distance.local_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  | `4` |  | Maximum ECMP for BGP multi-path. |
    | [<samp>bgp_graceful_restart</samp>](## "bgp_graceful_restart") | Dictionary |  |  |  | BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.<br>Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.<br> |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "bgp_graceful_restart.enabled") | Boolean | Required | `False` |  | Enable or disable graceful-restart for all BGP peers. |
    | [<samp>&nbsp;&nbsp;restart_time</samp>](## "bgp_graceful_restart.restart_time") | Integer |  | `300` | Min: 1<br>Max: 3600 | Restart time in seconds. |
    | [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  | `4` | Min: 1<br>Max: 512 | Maximum Paths for BGP multi-path. |
    | [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  | Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.<br>Note that the name of the peer groups use '-' instead of '_' in EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | `IPv4-UNDERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.ipv4_underlay_peers.bfd") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipv4_underlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | `MLAG-IPv4-UNDERLAY-PEER` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.bfd") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | `EVPN-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.evpn_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | `EVPN-OVERLAY-CORE` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.evpn_overlay_core.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_core.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;mpls_overlay_peers</samp>](## "bgp_peer_groups.mpls_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mpls_overlay_peers.name") | String |  | `MPLS-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mpls_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.mpls_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mpls_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;rr_overlay_peers</samp>](## "bgp_peer_groups.rr_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.rr_overlay_peers.name") | String |  | `RR-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.rr_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.rr_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.rr_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;ipvpn_gateway_peers</samp>](## "bgp_peer_groups.ipvpn_gateway_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.name") | String |  | `IPVPN-GATEWAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.ipv4_underlay_peers</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.mlag_ipv4_underlay_peer</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.evpn_overlay_peers</samp> instead.</span> |
    | [<samp>bgp_update_wait_install</samp>](## "bgp_update_wait_install") | Boolean |  |  |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br> |
    | [<samp>bgp_update_wait_for_convergence</samp>](## "bgp_update_wait_for_convergence") | Boolean |  |  |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br> |

=== "YAML"

    ```yaml
    # AS number to use to configure overlay when "overlay_routing_protocol" == ibgp.
    bgp_as: <str>

    # Default activation of IPv4 unicast address-family on all IPv4 neighbors.
    # It is best practice to disable activation.
    bgp_default_ipv4_unicast: <bool; default=False>
    bgp_distance:
      external_routes: <int; 1-255; required>
      internal_routes: <int; 1-255; required>
      local_routes: <int; 1-255; required>

    # Maximum ECMP for BGP multi-path.
    bgp_ecmp: <int; default=4>

    # BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.
    # Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.
    bgp_graceful_restart:

      # Enable or disable graceful-restart for all BGP peers.
      enabled: <bool; default=False; required>

      # Restart time in seconds.
      restart_time: <int; 1-3600; default=300>

    # Maximum Paths for BGP multi-path.
    bgp_maximum_paths: <int; 1-512; default=4>

    # Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
    # Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
    bgp_peer_groups:
      ipv4_underlay_peers:

        # Name of peer group.
        name: <str; default="IPv4-UNDERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=False>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      mlag_ipv4_underlay_peer:

        # Name of peer group.
        name: <str; default="MLAG-IPv4-UNDERLAY-PEER">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=False>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      evpn_overlay_peers:

        # Name of peer group.
        name: <str; default="EVPN-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      evpn_overlay_core:

        # Name of peer group.
        name: <str; default="EVPN-OVERLAY-CORE">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      mpls_overlay_peers:

        # Name of peer group.
        name: <str; default="MPLS-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      rr_overlay_peers:

        # Name of peer group.
        name: <str; default="RR-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      ipvpn_gateway_peers:

        # Name of peer group.
        name: <str; default="IPVPN-GATEWAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>

    # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
    # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
    bgp_update_wait_install: <bool>

    # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
    bgp_update_wait_for_convergence: <bool>
    ```
