#!/usr/bin/python3

# Ansible Imports
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.eveng import check_eveng_connection
from ansible.module_utils.eveng import check_eveng_password


__metaclass__ = type

DOCUMENTATION = ""

EXAMPLES = ""


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        host=dict(type='str'),
        username=dict(type='str'),
        password=dict(type='str')
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message='',
        http_reachability=False,
        http_default_password=False,
        http_custom_password=False,
        https_reachability=False,
        https_default_password=False,
        https_custom_password=False,
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

    # Main flow starts here

    # vars init

    host = module.params['host']
    username = module.params['username']
    password = module.params['password']
    default_password = 'eve'
    protocols = ['http', 'https']

    # Test cases
    # Test HTTP connection 
    for protocol in protocols:
        # Check connection for the given protocol
        if check_eveng_connection(host=host, protocol=protocol):
            result[f'{protocol}_reachability'] = True

            # Check default password for the protocol
            if check_eveng_password(host=host, username=username, password=default_password, protocol=protocol):
                result[f'{protocol}_default_password'] = True

            # Check custom password for the protocol
            if check_eveng_password(host=host, username=username, password=password, protocol=protocol):
                result[f'{protocol}_custom_password'] = True

    result['message'] = 'OK'

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result, **ansible_facts)


def main():
    run_module()


if __name__ == '__main__':
    main()
