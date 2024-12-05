#!/usr/bin/python3

# Ansible Imports
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.eveng import eveng_connect
from ansible.module_utils.eveng import change_admin_password

__metaclass__ = type

DOCUMENTATION = ""

EXAMPLES = ""


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        host=dict(type='str'),
        username=dict(type='str'),
        password=dict(type='str'),
        new_password=dict(type='str')
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

    # Main flow starts here

    # vars init

    host = module.params['host']
    username = module.params['username']
    password = module.params['password']
    new_password = module.params['new_password']

    # create connection
    conn = eveng_connect(host=host, username=username, password=password)

    try:
        change_password = change_admin_password(conn=conn, new_password=new_password)
        if change_password.get('status') != 'success':
            module.fail_json(msg=f"Password Change failed: {change_password.get('message')}", **result)

    except Exception as e:
        module.fail_json(msg=f"Error occurred: {e}", **result)
      
    result['message'] = 'OK'

    conn.logout()
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result, **ansible_facts)


def main():
    run_module()

if __name__ == '__main__':
    main()
