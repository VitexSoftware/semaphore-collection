import time
import semaphore_client
from semaphore import schedule_api
from semaphore_client.model.schedule_request import ScheduleRequest
from semaphore_client.model.schedule import Schedule
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
    api_instance = schedule_api.ScheduleApi(api_client)
    project_id = 1 # int | Project ID
    schedule = ScheduleRequest(
        id=1,
        cron_format="* * * 1 *",
        project_id=1,
        template_id=1,
    ) # ScheduleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # create schedule
        api_response = api_instance.project_project_id_schedules_post(project_id, schedule)
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling ScheduleApi->project_project_id_schedules_post: %s\n" % e)