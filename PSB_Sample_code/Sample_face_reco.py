'''
Important Libraries

'''
import logging
import asyncio

import mini.mini_sdk as Mini
from mini.dns.dns_browser import WiFiDevice
'''
Important Libraries

'''

'''
AlphaMini Libraries

'''
from mini.apis.api_observe import ObserveFaceRecognise
from mini.pb2.codemao_facerecognisetask_pb2 import FaceRecogniseTaskResponse
from mini.apis import errors
from mini.apis.api_sound import StartPlayTTS, StopPlayTTS, ControlTTSResponse
from mini.apis.api_sound import StopAllAudio, StopAudioResponse
from mini.apis.base_api import MiniApiResultType

'''
AlphaMini Libraries

'''

#logging information 
Mini.set_log_level(logging.INFO)
Mini.set_log_level(logging.DEBUG)
Mini.set_robot_type(Mini.RobotType.EDU) #AlphaMini Overseased, declaration -> Important


#Function for Text to Speech.
async def _play_tts():
    block: StartPlayTTS = StartPlayTTS(text="Detected a Face") #Edit the " " for different speech.
    (resultType, response) = await block.execute()
    print(f'{response}')
    return()


async def test_ObserveFaceRecognise():

    observer: ObserveFaceRecognise = ObserveFaceRecognise()

    # FaceRecogniseTaskResponse.faceInfos: [FaceInfoResponse]
    # FaceInfoResponse.id, FaceInfoResponse.name,FaceInfoResponse.gender,FaceInfoResponse.age
    # FaceRecogniseTaskResponse.isSuccess
    # FaceRecogniseTaskResponse.resultCode


    def handler(msg: FaceRecogniseTaskResponse):
        print(f"{msg}")
        asyncio.create_task(_play_tts())
        if msg.isSuccess and msg.faceInfos:
            observer.stop()
            

    observer.set_handler(handler)
    observer.start()
    await asyncio.sleep(0)

'''

Connection Initialization Code (Computer to AlphaMini).

'''

#Function for Finding Device -> Important 
async def get_device_by_name():
    result: WiFiDevice = await Mini.get_device_by_name("00358", 10)  #Please enter AlphaMini-Robot ID  "00352"
    print(f"test_get_device_by_name result:{result}")
    return result

#Function for Binding Device with Computer-> Important 
async def connection(dev: WiFiDevice) -> bool:
    return await Mini.connect(dev)



#Function for starting a main Progarm loop -> Important
async def start_run_program():
    await Mini.enter_program()


#Function for Shutdown Progarm -> Important
async def shutdown():
    await Mini.quit_program()
    await Mini.release()

'''

Connection Initialization Code (Computer to AlphaMini).

'''


#Main Function

if __name__ == '__main__':
    device: WiFiDevice = asyncio.get_event_loop().run_until_complete(get_device_by_name())
    if device:
        asyncio.get_event_loop().run_until_complete(connection(device))
        asyncio.get_event_loop().run_until_complete(start_run_program())
        asyncio.get_event_loop().run_until_complete(test_ObserveFaceRecognise())
        # 定义了事件监听对象,必须让event_loop.run_forver()
        asyncio.get_event_loop().run_forever()
        asyncio.get_event_loop().run_until_complete(shutdown())







