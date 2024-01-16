<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_ssh_client_source_interfaces</samp>](## "ip_ssh_client_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_ssh_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_ssh_client_source_interfaces.[].vrf") | String |  | `default` |  |  |

=== "YAML"

    ```yaml
    ip_ssh_client_source_interfaces:

        # Interface Name
      - name: <str>
        vrf: <str; default="default">
    ```
