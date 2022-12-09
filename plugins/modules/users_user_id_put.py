import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.user_put_request import UserPutRequest
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
    api_instance = user_api.UserApi(api_client)
    user_id = 2 # int | User ID
    user = UserPutRequest(
        name="Integration Test User2",
        username="test-user2",
        email="test2@ansiblesemaphore.test",
        alert=True,
        admin=True,
    ) # UserPutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates user details
        api_instance.users_user_id_put(user_id, user)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_user_id_put: %s\n" % e)