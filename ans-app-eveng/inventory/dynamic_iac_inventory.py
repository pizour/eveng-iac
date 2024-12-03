#!/usr/bin/env python

import yaml
import json

def load_yaml_inventory():
    # Open the YAML file that contains your inventory
    with open('../tf_infra_iac.yml', 'r') as file:
        inventory_data = yaml.safe_load(file)
    
    return inventory_data

def main():
    # Load inventory from YAML
    inventory = load_yaml_inventory()

    # Generate hosts and hostvars
    hosts = {}
    for vm in inventory.get("infra", {}).get("vms", []):
        alias = f'{vm.get("unique_vm_alias")}.{inventory["infra"]["azure_location"]}.cloudapp.azure.com'
        hosts[alias] = {
            'vm_name': vm.get("vm_name"),
            'ansible_user': vm.get("ssh_username"),
            'ssh_pubkey': vm.get("ssh_pubkey")
        }

    output = {
        'all': {
            'hosts': list(hosts.keys())
        },
        '_meta': {
            'hostvars': hosts
        }
    }

    # Print the JSON-formatted output
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
