from ncclient import manager
import logging
import argparse

# logging.basicConfig(level=logging.DEBUG)

# Set up argument parser
parser = argparse.ArgumentParser(description="NETCONF script to configure network devices.")
parser.add_argument("--host", required=True, help="Hostname or IP address of the NETCONF server")
parser.add_argument("--port", type=int, default=2222, help="Port number of the NETCONF server")
parser.add_argument("--username", required=True, help="Username for NETCONF authentication")
parser.add_argument("--password", required=True, help="Password for NETCONF authentication")
parser.add_argument("--config-file", help="Path to the configuration file")

args = parser.parse_args()

# Default configuration
default_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
    <interface-configuration>
      <active>act</active>
      <interface-name>GigabitEthernet0/0/0/1</interface-name>
      <description>Configured via NETCONF</description>
    </interface-configuration>
  </interface-configurations>
</config>
"""

# Read configuration from file if provided
if args.config_file:
    with open(args.config_file, 'r') as file:
        config = file.read()
else:
    config = default_config

with manager.connect(host=args.host, port=args.port, username=args.username, password=args.password, hostkey_verify=False) as m:
    m.edit_config(target="candidate", config=config)
    m.commit()
    print("✅ Netconf Applied Successfully")