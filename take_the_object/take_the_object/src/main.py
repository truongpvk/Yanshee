from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

robo_ip = '10.220.5.230' # Change to robot API

right_arm_servos = ['RightShoulderRoll', 'RightShoulderFlex', 'RightElbowFlex']
left_arm_servos = ['LeftShoulderRoll', 'LeftShoulderFlex', 'LeftElbowFlex']
right_foot_servos = ['RightHipLR', 'RightHipFB', 'RightKneeFlex', 'RightAnkleFB', 'RightAnkleUD']
left_foot_servos = ['LeftHipLR', 'LeftHipFB', 'LeftKneeFlex', 'LeftAnkleFB', 'LeftAnkleUD']

servos = right_arm_servos + left_arm_servos + right_foot_servos + left_foot_servos + ['NeckLR']

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = f'http://{robo_ip}:9090/v1'
api_instance = openadk.ServosApi(openadk.ApiClient(configuration)) # Change API options

def putServo(angles: dict, runtime=1000):
    body = {
        'runtime': runtime,
        'angles': angles,
    }

    api_response = api_instance.put_servos_angles(body)
    return api_response

def putRightArm(shoulderRoll=90, shoulderFlex=141, elbowFlex=166):
    return {
        right_arm_servos[0]: shoulderRoll,
        right_arm_servos[1]: shoulderFlex,
        right_arm_servos[2]: elbowFlex,
    }

def putLeftArm(shoulderRoll=90, shoulderFlex=40, elbowFlex=15):
    return {
        left_arm_servos[0]: shoulderRoll,
        left_arm_servos[1]: shoulderFlex,
        left_arm_servos[2]: elbowFlex,
    }

def putRightFoot(hipLR=90, hipFB=61, knee=76, ankleFB=111,ankleUD=90):
    return {
        right_foot_servos[0]: hipLR,
        right_foot_servos[1]: hipFB,
        right_foot_servos[2]: knee,
        right_foot_servos[3]: ankleFB,
        right_foot_servos[4]: ankleUD,
    }

def putLeftFoot(hipLR=90, hipFB=120, knee=106, ankleFB=71,ankleUD=90):
    return {
        left_foot_servos[0]: hipLR,
        left_foot_servos[1]: hipFB,
        left_foot_servos[2]: knee,
        left_foot_servos[3]: ankleFB,
        left_foot_servos[4]: ankleUD,
    }
actions = []

def addAction(servo: dict):
    global actions

    actions.append(servo)

addAction({**putRightArm(89,23,85), **putLeftArm(89,153, 92)})
addAction({**putRightArm(180,23,85), **putLeftArm(0,160, 92)})
addAction({**putRightArm(180,40,28), **putLeftArm(0,147, 131)})
addAction({**putRightArm(180,15,18), **putLeftArm(0,174, 153)})
addAction({**putRightArm(86,15,18), **putLeftArm(93,174, 153)})
addAction({**putRightArm(180,15,18), **putLeftArm(0,174, 153)})
addAction({**putRightArm(180,40,28), **putLeftArm(0,147, 131)})

for action in actions:
    response = putServo(action)
    print(response)
    time.sleep(5)