#!/usr/bin/python

"""Obtain Semaphore info."""

from __future__ import (absolute_import, division, print_function)

import os

from ansible.module_utils.basic import AnsibleModule


import semaphore_client


from semaphore_client.model.info_type import InfoType
from semaphore_client.semaphore import default_api


'''
Copyright: (c) 2022, Vítězslav Dvořák <vitex@vitexsoftware.com>
GNU General Public License v3.0+ 
(see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
'''

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'], 'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: info

short_description: Semaphore info

version_added: "1.0.0"

description: Fetches information about semaphore.

options:
    semaphore_uri:
        description: Location of Sempaphore Server API
        requied: false
        type: string
        example: https://demo.ansible-semaphore.com/api
    sempaphore_token:
        description: Bearer token for your Sempaphore Server API
        requied: false
        type: string
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - vitexsoftware.semaphore.my_doc_fragment_name

author:
    - Vítězslav Dvořák (@Vitexus)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  vitexsoftware.semaphore.info:
    semaphore_uri: https://demo.ansible-semaphore.com/api
    semaphore_token: vku6sucjo96pkymjwzzfakqpo2gkij5svvfb_ynipuw=
'''

RETURN = r'''
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''


def run_module():
    """Obtain Semaphore Info."""
    module_args = dict(
        semaphore_uri=dict(type='str', required=True,
                           default=os.environ.get('SEMAPHORE_URI')),
        semaphore_token=dict(type='str', required=True,
                             default=os.environ.get('SEMAPHORE_TOKEN'),
                             no_log=True),
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    configuration = semaphore_client.Configuration(
        host=module.params['semaphore_uri']
    )
    configuration.api_key['bearer'] = module.params['semaphore_token']

    with semaphore_client.ApiClient(configuration) as api_client:
        api_instance = default_api.DefaultApi(api_client)
        try:
            api_response = api_instance.info_get()

            result['message'] = api_response
        except semaphore_client.ApiException as e:
            module.fail_json(msg="Exception when calling DefaultApi->info_get: ", **e)

    result['changed'] = False

    module.exit_json(**result)


def main():
    """Do Module Info."""
    run_module()


if __name__ == '__main__':
    main()
