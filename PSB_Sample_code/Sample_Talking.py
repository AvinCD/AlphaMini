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
    block: StartPlayTTS = StartPlayTTS(text="Hello! We are  R A I Students, In PSB Academy") #Edit the " " for different speech.
    (resultType, response) = await block.execute()
    print(f'{response}')
    return()




'''

Connection Initialization Code (Computer to AlphaMini).

'''

#Function for Finding Device -> Important 
async def get_device_by_name():
    result: WiFiDevice = await Mini.get_device_by_name("00352", 10)  #Please enter AlphaMini-Robot ID  "00352"
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
async def main():
    device: WiFiDevice = await get_device_by_name()
    if device:
        await connection(device)
        await start_run_program()
        await _play_tts()
        await shutdown()

if __name__ == '__main__' :
    asyncio.run(main())







