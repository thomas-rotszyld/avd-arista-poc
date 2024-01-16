#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_ospf_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: eos_ospf_interfaces
version_added: 1.1.0
short_description: OSPF Interfaces Resource Module.
description:
- This module manages OSPF configuration of interfaces on devices running Arista EOS.
author: Gomathi Selvi Srinivasan (@GomathiselviS)
options:
  config:
    description: A list of OSPF configuration for interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name/Identifier of the interface.
        type: str
      address_family:
        description:
        - OSPF settings on the interfaces in address-family context.
        type: list
        elements: dict
        suboptions:
          afi:
            description:
            - Address Family Identifier (AFI) for OSPF settings on the interfaces.
            type: str
            choices: ['ipv4', 'ipv6']
            required: true
          area:
            description:
            - Area associated with interface.
            - Valid only when afi = ipv4.
            type: dict
            suboptions:
              area_id:
                description:
                - Area ID as a decimal or IP address format.
                type: str
                required: true
          authentication_v2:
            description:
            - Authentication settings on the interface.
            - Valid only when afi = ipv4.
            type: dict
            suboptions:
              message_digest:
                description:
                - Use message-digest authentication.
                type: bool
              set:
                description:
                - Enable authentication on the interface.
                type: bool
          authentication_v3:
            description:
            - Authentication settings on the interface.
            - Valid only when afi = ipv6.
            type: dict
            suboptions:
              spi:
                description: IPsec Security Parameter Index.
                type: int
              algorithm:
                description: Encryption alsgorithm.
                type: str
                choices: ["md5", "sha1"]
              keytype:
                description:
                - Specifies if an unencrypted/hidden follows.
                - 0 denotes unencrypted key.
                - 7 denotes hidden key.
                type: str
              passphrase:
                description: Passphrase String for deriving keys for authentication and encryption.
                type: str
              key:
                description: 128 bit MD5 key or 140 bit SHA1 key.
                type: str
          authentication_key:
            description:
            - Configure the authentication key for the interface.
            - Valid only when afi = ipv4.
            type: dict
            suboptions:
              encryption:
                description:
                - 0 Specifies an UNENCRYPTED authentication key will follow.
                - 7 Specifies a proprietry encryption type.`
                type: str
              key:
                description:
                - password (up to 8 chars).
                type: str
          bfd:
            description: Enable BFD.
            type: bool
          cost:
            description:
            - metric associated with interface.
            type: int
          dead_interval:
            description:
            - Time interval to detect a dead router.
            type: int
          encryption_v3:
            description:
            - Authentication settings on the interface.
            - Valid only when afi = ipv6.
            type: dict
            suboptions:
              spi:
                description: IPsec Security Parameter Index.
                type: int
              encryption:
                description: encryption type.
                choices: ["3des-cbc", "aes-128-cbc", "aes-192-cbc", "aes-256-cbc", "null"]
                type: str
              algorithm:
                description: algorithm.
                type: str
                choices: ["md5", "sha1"]
              keytype:
                description:
                - Specifies if an unencrypted/hidden follows.
                - 0 denotes unencrypted key.
                - 7 denotes hidden key.
                type: str
              passphrase:
                description: Passphrase String for deriving keys for authentication and encryption.
                type: str
              key:
                description: key
                type: str
          hello_interval:
            description:
            - Timer interval between transmission of hello packets.
            type: int
          ip_params:
            description:
            - Specify parameters for IPv4/IPv6.
            - Valid only when afi = ipv6.
            type: list
            elements: dict
            suboptions:
              afi:
                description:
                - Address Family Identifier (AFI) for OSPF settings on the interfaces.
                type: str
                choices: ['ipv4', 'ipv6']
                required: true
              area:
                description:
                - Area associated with interface.
                - Valid only when afi = ipv4.
                type: dict
                suboptions:
                  area_id:
                    description:
                    - Area ID as a decimal or IP address format.
                    type: str
                    required: true
              bfd:
                description: Enable BFD.
                type: bool
              cost:
                description:
                - metric associated with interface.
                type: int
              dead_interval:
                description:
                - Time interval to detect a dead router.
                type: int
              hello_interval:
                description:
                - Timer interval between transmission of hello packets.
                type: int
              mtu_ignore:
                description:
                - if true, Disable MTU check for Database Description packets.
                type: bool
              network:
                description:
                - Interface type.
                type: str
              priority:
                description:
                - Interface priority.
                type: int
              retransmit_interval:
                description:
                - LSA retransmission interval.
                type: int
              passive_interface:
                description:
                - Suppress routing updates in an interface.
                type: bool
              transmit_delay:
                description:
                - LSA transmission delay.
                type: int
          message_digest_key:
            description:
            - Message digest authentication password (key) settings.
            type: dict
            suboptions:
              key_id:
                description:
                - Key ID.
                type: int
              encryption:
                description:
                - 0 Specifies an UNENCRYPTED ospf password (key) will follow.
                - 7 Specifies a proprietry encryption type.
                type: str
              key:
                description:
                - Authentication key (upto 16 chars).
                type: str
          mtu_ignore:
            description:
            - if true, Disable MTU check for Database Description packets.
            type: bool
          network:
            description:
            - Interface type.
            type: str
          passive_interface:
            description:
            - Suppress routing updates in an interface.
            - Valid only when afi = ipv6.
            type: bool
          priority:
            description:
            - Interface priority.
            type: int
          retransmit_interval:
            description:
            - LSA retransmission interval.
            type: int
          shutdown:
            description:
            - Shutdown OSPF on this interface.
            type: bool
          transmit_delay:
            description:
            - LSA transmission delay.
            type: int
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the EOS device by
      executing the command B(show running-config | section interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str

  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - parsed
    - rendered
    default: merged
"""

EXAMPLES = """

# Using merged

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# veos(config)#

- name: Merge provided configuration with device configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv4"
            area:
              area_id: "0.0.0.50"
            cost: 500
            mtu_ignore: true
          - afi: "ipv6"
            dead_interval: 44
            ip_params:
              - afi: "ipv6"
                mtu_ignore: true
                network: "point-to-point"
    state: merged

# Task output:
# ------------
# before: []
#
# commands:
# - interface Vlan1
# - ip ospf area 0.0.0.50
# - ip ospf cost 500
# - ip ospf mtu-ignore
# - ospfv3 dead-interval 44
# - ospfv3 ipv6 mtu-ignore
# - ospfv3 ipv6 network point-to-point
#
# after:
#   - address_family:
#     - afi: ipv4
#       area:
#         area_id: 0.0.0.50
#       cost: 500
#       mtu_ignore: true
#     - afi: ipv6
#       dead_interval: 44
#       ip_params:
#       - afi: ipv6
#         mtu_ignore: true
#         network: point-to-point
#     name: Vlan1

# After state:
# ------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf cost 500
#    ip ospf mtu-ignore
#    ip ospf area 0.0.0.50
#    ospfv3 dead-interval 44
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore

# Using replaced

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf cost 500
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ip ospf area 0.0.0.50
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 dead-interval 44
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: Replace device configuration with provided configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv6"
            cost: 44
            bfd: true
            ip_params:
              - afi: "ipv6"
                mtu_ignore: true
                network: "point-to-point"
                dead_interval: 56
    state: replaced

# Task output:
# ------------
# before:
#   - address_family:
#     - afi: ipv4
#       area:
#         area_id: 0.0.0.50
#       cost: 500
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       cost: 106
#       dead_interval: 44
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2
#
# commands:
# - interface Vlan1
# - no ip ospf cost 500
# - no ip ospf dead-interval 29
# - no ip ospf hello-interval 66
# - no ip ospf mtu-ignore
# - no ip ospf area 0.0.0.50
# - ospfv3 cost 44
# - ospfv3 bfd
# - ospfv3 authentication ipsec spi 30 md5 passphrase 7 7hl8FV3lZ6H1mAKpjL47hQ==
# - no ospfv3 ipv4 priority 45
# - no ospfv3 ipv4 area 0.0.0.5
# - ospfv3 ipv6 dead-interval 56
# - no ospfv3 ipv6 passive-interface
# - no ospfv3 ipv6 retransmit-interval 115
# - no ospfv3 hello-interval 77
# - no ospfv3 dead-interval 44
# - no ospfv3 transmit-delay 100
#
# after:
#   - address_family:
#     - afi: ipv6
#       bfd: true
#       cost: 44
#       ip_params:
#       - afi: ipv6
#         mtu_ignore: true
#         network: point-to-point
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# After state:
# ------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ospfv3 bfd
#    ospfv3 cost 44
#    no ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

# Using overidden

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ospfv3 bfd
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: Override device configuration with provided configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv6"
            cost: 44
            bfd: true
            ip_params:
              - afi: "ipv6"
                mtu_ignore: true
                network: "point-to-point"
                dead_interval: 56
    state: overridden

# Task output:
# ------------
# before:
#   - address_family:
#     - afi: ipv4
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       bfd: true
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2
#
# commands:
# - interface Vlan2
# - no ospfv3 ipv4 hello-interval 45
# - no ospfv3 ipv4 retransmit-interval 100
# - no ospfv3 ipv4 area 0.0.0.6
# - interface Vlan1
# - no ip ospf dead-interval 29
# - no ip ospf hello-interval 66
# - no ip ospf mtu-ignore
# - ospfv3 cost 44
# - ospfv3 authentication ipsec spi 30 md5 passphrase 7 7hl8FV3lZ6H1mAKpjL47hQ==
# - no ospfv3 ipv4 priority 45
# - no ospfv3 ipv4 area 0.0.0.5
# - no ospfv3 ipv6 passive-interface
# - no ospfv3 ipv6 retransmit-interval 115
# - no ospfv3 hello-interval 77
# - no ospfv3 transmit-delay 100
#
# after:
#   - address_family:
#     - afi: ipv6
#       bfd: true
#       cost: 44
#       ip_params:
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#     name: Vlan1

# After state:
# ------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ospfv3 bfd
#    ospfv3 cost 44
#    no ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore

# Using deleted

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ospfv3 bfd
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: Delete provided ospf interface config
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
    state: deleted

# Task output:
# ------------
# before:
#   - address_family:
#     - afi: ipv4
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       bfd: true
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# commands:
# - interface Vlan1
# - no ip ospf dead-interval 29
# - no ip ospf hello-interval 66
# - no ip ospf mtu-ignore
# - no ospfv3 bfd
# - no ospfv3 cost 106
# - no ospfv3 hello-interval 77
# - no ospfv3 transmit-delay 100
# - no ospfv3 ipv4 priority 45
# - no ospfv3 ipv4 area 0.0.0.5
# - no ospfv3 ipv6 passive-interface
# - no ospfv3 ipv6 dead-interval 56
# - no ospfv3 ipv6 retransmit-interval 115
# - no ospfv3 ipv6 network point-to-point
# - no ospfv3 ipv6 mtu-ignore
#
# after:
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# After state:
# ------------
# veos#show running-config | section interface | ospf
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

# Using parsed

# parsed.cfg
# ----------
# interface Vlan1
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ip ospf cost 500
#    ospfv3 bfd
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6
#

- name: parse provided config into structured facts
  arista.eos.eos_ospf_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Task output:
# ------------
# parsed:
#   - address_family:
#     - afi: ipv4
#       cost: 500
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       bfd: true
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# Using gathered:

# Device config:
# veos#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf cost 500
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ip ospf area 0.0.0.50
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: gather runnig config
  arista.eos.eos_ospf_interfaces:
    state: gathered

# Task output:
# ------------
# gathered:
#   - address_family:
#     - afi: ipv4
#       area:
#         area_id: 0.0.0.50
#       cost: 500
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# Using rendered

- name: Render provided configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv4"
            dead_interval: 29
            mtu_ignore: true
            hello_interval: 66
          - afi: "ipv6"
            hello_interval: 77
            cost: 106
            transmit_delay: 100
            ip_params:
              - afi: "ipv6"
                retransmit_interval: 115
                dead_interval: 56
                passive_interface: true
              - afi: "ipv4"
                area:
                  area_id: "0.0.0.5"
                priority: 45
      - name: "Vlan2"
        address_family:
          - afi: "ipv6"
            ip_params:
              - afi: "ipv4"
                area:
                  area_id: "0.0.0.6"
                hello_interval: 45
                retransmit_interval: 100
          - afi: "ipv4"
            message_digest_key:
              key_id: 200
              encryption: 7
              key: "hkdfhtu=="

    state: rendered

# Task output:
# ------------
# rendered:
# - interface Vlan1
# - ip ospf dead-interval 29
# - ip ospf mtu-ignore
# - ip ospf hello-interval 66
# - ospfv3 hello-interval 77
# - ospfv3 cost 106
# - ospfv3 transmit-delay 100
# - ospfv3 ipv4 area 0.0.0.5
# - ospfv3 ipv4 priority 45
# - ospfv3 ipv6 retransmit-interval 115
# - ospfv3 ipv6 dead-interval 56
# - ospfv3 ipv6 passive-interface
# - interface Vlan2
# - ip ospf message-digest-key 200 md5 7 hkdfhtu==
# - ospfv3 ipv4 area 0.0.0.6
# - ospfv3 ipv4 hello-interval 45
# - ospfv3 ipv4 retransmit-interval 100
"""
RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - interface Vlan1
    - ip ospf dead-interval 29
    - ip ospf mtu-ignore
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - interface Vlan1
    - ip ospf dead-interval 29
    - ip ospf mtu-ignore
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.ospf_interfaces.ospf_interfaces import (
    Ospf_interfacesArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.ospf_interfaces.ospf_interfaces import (
    Ospf_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Ospf_interfacesArgs.argument_spec,
        mutually_exclusive=[],
        required_if=[],
        supports_check_mode=False,
    )

    result = Ospf_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
