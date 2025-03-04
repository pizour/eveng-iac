#!/usr/bin/python3

# Ansible Imports
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
import gdown
import tarfile
import os


__metaclass__ = type

DOCUMENTATION = ""

EXAMPLES = ""


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        url=dict(type='str'),
        destination=dict(type='str')
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

    def download_image(url, destination):

        output = f'{destination}/download.tgz'
        gdown.download(url, output, quiet=False)

        # Open and extract
        with tarfile.open(output, "r:gz") as tar:
            tar.extractall(destination)

        if os.path.exists(output):
            os.remove(output)
    
        return True


    # Main flow starts here

    # vars init
    url = module.params['url']
    destination = module.params['destination']

    resp = download_image(url=url, destination=destination)

    result['message'] = 'Image downloaded'
    result['changed'] = resp

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result, **ansible_facts)


def main():
    run_module()


if __name__ == '__main__':
    main()
