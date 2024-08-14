from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

robo_ip = '10.220.5.226'

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = f'http://{robo_ip}:9090/v1'
api_instance = openadk.MotionsApi(openadk.ApiClient(configuration))

#Thiết lập chuyển động
def motion_control(name: str, direction: str, repeat=1, speed='normal'):
    return {
        'name': name,
        'direction': direction,
        'repeat': repeat,
        'speed': speed
    }

def body_define(motion: dict, operation='start', timestamp=2000):
    return {
        'operation': operation,
        'motion': motion,
        'timestamp': timestamp
    }

#Gọi API thực hiện chuyển động
def putMotion(body):
    global api_instance

    try:
        # Get system's battery information
        api_response = api_instance.put_motions(body)
        print(api_response)
    except ApiException as e:
        print("Exception when calling putMotionsApi: %s" % e)

def stopMotion():
    api_response = api_instance.put_motions(body_define(motion_control('walk', 'left'), operation='stop'))
    print(api_response)

stopMotion()