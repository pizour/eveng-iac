#!/usr/bin/python3

# Ansible Imports
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
from evengsdk.client import EvengClient

__metaclass__ = type

DOCUMENTATION = ""

# EXAMPLES = '''
# - name: Allocate free cpus
#   libvirt_cpu_pinning:
#     allocate_cpus: 4
#     hypervisor_total_cpus: 64
#     hypervisor_reserved_cpus: [2, 3, 4, 59, 60, 61, 62, 63]
#   register: found_cpus
# '''


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        host=dict(type='str'),
        username=dict(type='str'),
        password=dict(type='str'),
        nodes=dict(type='list'),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message=''
    )

    # seed the ansible_facts dict
    ansible_facts = dict()

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    def eveng_connect(host,username,password):
        client = EvengClient(host=host)
        client.login(username=username, password=password)
        
        return client

    # Main flow starts here

    # vars init

    host = module.params['host']
    username = module.params['username']
    password = module.params['password']
    nodes = module.params['nodes']

    # create connection
    conn = eveng_connect(host=host, username=username, password=password)

    for node in nodes:
        resp = conn.api.node_template_detail(node_type=node['platform'])
        platform_version = f"{node['platform']}-{node['version']}"
        node['platform_version'] = platform_version
        if platform_version in resp['data']['options']['image']['list']:
            node['firmware_present'] = True
        else:
            node['firmware_present'] = False
        

    ansible_facts= dict(nodes=nodes)
    result['message'] = 'OK'

    conn.logout()
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result, **ansible_facts)


def main():
    run_module()


if __name__ == '__main__':
    main()
