#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

import os

from ansible.module_utils.basic import AnsibleModule

import semaphore_client

from semaphore_client.model.task import Task
from semaphore_client.semaphore import project_api
from semaphore_client.model.project_project_id_tasks_get_request import ProjectProjectIdTasksGetRequest

# Copyright: (c) 2022, Vítězslav Dvořák <vitex@vitexsoftware.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'], 'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: task

short_description: launch semaphore task

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Ansible way how to launch Task in semaphore.

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
    project_id:
        description: ID Of project containing task to launch
        requied: false
        type: string
    debug:
        requied: false
        type: bool
    dry_run:
        description: Use Dry Run capability
        requied: false
        type: string
    playbook:
        description: Name of playbook to run
        requied: false
        type: str
    environment:
        description: Name of environment used
        requied: false
        type: str
    template_id:
        description: Id Of template to launch.
        required: true
        type: int
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
  vitexsoftware.semaphore-api.task:
    template_id: 123
'''

RETURN = r'''
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''


def run_module():
    """Run Module main function."""
    module_args = dict(
        project_id=dict(type='int', required=True),
        debug=dict(type='bool', default=False),
        template_id=dict(type='int', required=True),
        dry_run=dict(type='bool', default=True),
        playbook=dict(type='str', required=True),
        environment=dict(type='str', required=True),
        semaphore_uri=dict(type='str',
                           default=os.environ.get('SEMAPHORE_URI')),
        semaphore_token=dict(type='str', default=os.environ.get(
            'SEMAPHORE_TOKEN'), no_log=True)
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

    if module.check_mode:
        module.exit_json(**result)

    configuration = semaphore_client.Configuration(
        host=module.params['semaphore_uri']
    )
    configuration.api_key['bearer'] = module.params['semaphore_token']

    with semaphore_client.ApiClient(configuration) as api_client:
        api_instance = project_api.ProjectApi(api_client)

        task = ProjectProjectIdTasksGetRequest(
            template_id=module.params['template_id'],
            debug=module.params['debug'],
            dry_run=module.params['dry_run'],
            playbook=module.params['playbook'],
            environment=module.params['environment'],
        )  # ProjectProjectIdTasksGetRequest |

        try:
            # Starts a job
            api_response = api_instance.project_project_id_tasks_post(
                module.params['project_id'], task)

            result['message'] = api_response
        except semaphore_client.ApiException as e:
            fail = dict(reason=e.reason, status=e.status)
            module.fail_json(
                msg='Exception when calling ProjectApi->project_project_id_tasks_post:', **fail)

    # result['original_message'] = module.params['name']

    result['changed'] = True

    module.exit_json(**result)


def main():
    """Run module from here."""
    run_module()


if __name__ == '__main__':
    main()
