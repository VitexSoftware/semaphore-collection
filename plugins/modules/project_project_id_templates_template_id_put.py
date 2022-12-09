import time
import semaphore_client
from semaphore import project_api
from semaphore_client.model.template_request import TemplateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ansible-semaphore.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_client.Configuration(
    host = "https://demo.ansible-semaphore.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearer
configuration.api_key['bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    template_id = 7 # int | template ID
    template = TemplateRequest(
        project_id=1,
        inventory_id=1,
        repository_id=1,
        environment_id=1,
        view_id=1,
        alias="Test",
        playbook="test.yml",
        arguments="[]",
        description="Hello, World!",
        override_args=True,
    ) # TemplateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates template
        api_instance.project_project_id_templates_template_id_put(project_id, template_id, template)
    except semaphore_client.ApiException as e:
        print("Exception when calling ProjectApi->project_project_id_templates_template_id_put: %s\n" % e)