from __future__ import print_function
import time
import openadk
import cv2
from openadk.rest import ApiException
from pprint import pprint

robo_ip = '10.220.5.230' # Change to robot API

right_arm_servos = ['RightShoulderRoll', 'RightShoulderFlex', 'RightElbowFlex']
left_arm_servos = ['LeftShoulderRoll', 'LeftShoulderFlex', 'LeftElbowFlex']
right_foot_servos = ['RightHipLR', 'RightHipFB', 'RightKneeFlex', 'RightAnkleFB', 'RightAnkleUD']
left_foot_servos = ['LeftHipLR', 'LeftHipFB', 'LeftKneeFlex', 'LeftAnkleFB', 'LeftAnkleUD']
neck = ['NeckLR']

servos = right_arm_servos + left_arm_servos + right_foot_servos + left_foot_servos + neck

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = f'http://{robo_ip}:9090/v1'
api_instance = openadk.ServosApi(openadk.ApiClient(configuration))

servos_angle = []

while True:
    api_response = api_instance.get_servos_angles(right_arm_servos+left_arm_servos)
    servos_angle.append(api_response)
    print('Done!')

    continues = int(input('Continue? (0/1)'))

    if continues == 0:
        break

for angle in servos_angle:
    print(angle)