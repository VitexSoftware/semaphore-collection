import time
import semaphore_client
from semaphore import project_api
from semaphore_client.model.access_key_request import AccessKeyRequest
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
    access_key = AccessKeyRequest(
        name="None",
        type="none",
        project_id=1,
    ) # AccessKeyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add access key
        api_instance.project_project_id_keys_post(project_id, access_key)
    except semaphore_client.ApiException as e:
        print("Exception when calling ProjectApi->project_project_id_keys_post: %s\n" % e)
        