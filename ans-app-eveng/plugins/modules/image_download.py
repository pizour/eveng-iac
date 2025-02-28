#!/usr/bin/python3

# Ansible Imports
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
import requests
from urllib.parse import urlparse, parse_qs


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

        session = requests.Session()

        # Parse URL
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Extract Base URL and File ID
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        file_id = query_params.get("id", [""])[0]
       
        # Step 1: Get confirmation token
        response = session.get(base_url, params={'id': file_id}, stream=True)
        token = None

        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                token = value

        # Step 2: Download the file with confirmation token (if needed)
        params = {'id': file_id}
        if token:
            params['confirm'] = token

        response = session.get(base_url, params=params, stream=True)

        # Step 3: Save file in chunks
        with open(destination, "wb") as file:
            for chunk in response.iter_content(32768):  # 32 KB chunks
                if chunk:
                    file.write(chunk)
    
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
