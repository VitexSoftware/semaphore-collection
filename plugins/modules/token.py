#!/usr/bin/python

"""Create an API token."""

from __future__ import (absolute_import, division, print_function)

import os
import re

from ansible.module_utils.basic import AnsibleModule

import semaphore_client
from semaphore_client.model.login import Login
from semaphore_client.semaphore import authentication_api

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
        requied: true
        type: string
        example: https://demo.ansible-semaphore.com/api
    auth:
        description: Login Name
        requied: false
        type: string
    password:
        description: Semaphore user's password
        requied: false
        type: string

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - vitexsoftware.semaphore-api.my_doc_fragment_name

author:
    - Vítězslav Dvořák (@Vitexus)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  vitexsoftware.semaphore-api.info:
'''

RETURN = r'''
message:
    description: The output message that token module generates.
    type: str
    returned: always
    sample: 'goodbye'
token:
    description: Token string itself
    type: str
    returned: always
    sample: xiwci9xr2mjnfx1tnfyq_7pjo2maqdtoxj0cvz6e5tq=
created:
    description: Toke creation time
    type: str
    returned: always
    sample: 2022-12-11T19:50:20Z
expired:
    description: is token fresh enough ?
    type: bool
    returned: always
    sample: false,
user_id:
    description: User ID for token
    type: int
    returned: always
    sample: 1
'''


def run_module():
    """Login and query."""
    module_args = dict(
        auth=dict(type='str', required=True,
                  default=os.environ.get('SEMAPHORE_LOGIN')),
        password=dict(type='str', required=True, default=os.environ.get(
            'SEMAPHORE_PASSWORD'), no_log=True),
        semaphore_uri=dict(type='str', required=True,
                           default=os.environ.get('SEMAPHORE_URI'))
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    configuration = semaphore_client.Configuration(
        host=module.params['semaphore_uri']
        )

    with semaphore_client.ApiClient(configuration) as api_client:
        api_instance = authentication_api.AuthenticationApi(api_client)
        login_body = Login(
            auth=module.params['auth'],
            password=module.params['password'],
        )  # Login |

        try:
            api_instance.auth_login_post(login_body)
            matches = re.search('=(.*);', api_instance.api_client.last_response.getheader('set-cookie'))
            cookieAuth=matches.group(1)
            configuration2 = semaphore_client.Configuration(
                host=module.params['semaphore_uri'],
                api_key={'cookieAuth': cookieAuth},
                api_key_prefix={'cookieAuth': 'semaphore'}
                )
            configuration2.api_key['cookie'] = api_instance.api_client.last_response.getheader('set-cookie')

            try:
                with semaphore_client.ApiClient(configuration2) as api_client2:
                    api_instance2 = authentication_api.AuthenticationApi(api_client2)
                    api_response = api_instance2.user_tokens_post()
                result['message'] = 'Token obtained'
                result['token'] = api_response['id']
                result['created'] = api_response['created']
                result['expired'] = api_response['expired']
                result['user_id'] = api_response['user_id']
            except semaphore_client.ApiException as e:
                fail = dict(reason=e.reason, status=e.status)
                module.fail_json(
                    msg="Exception when calling AuthenticationApi->auth_login_post: ", **fail)

        except semaphore_client.ApiException as e:
            fail = dict(reason=e.reason, status=e.status)
            module.fail_json(
                msg="Exception when calling AuthenticationApi->auth_login_post: ", **fail)

    result['changed'] = True

    module.exit_json(**result)


def main():
    """Do Module Login."""
    run_module()


if __name__ == '__main__':
    main()
