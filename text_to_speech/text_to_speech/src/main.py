from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

robo_ip = '10.220.5.226' # Change to robot API

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = f'http://{robo_ip}:9090/v1'
api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) # Change API options

response = api_instance.get_devices_languages()
print(response)