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



#logging information 
Mini.set_log_level(logging.INFO)
Mini.set_log_level(logging.DEBUG)
Mini.set_robot_type(Mini.RobotType.EDU)  #AlphaMini Overseased, declaration -> Important



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



#Main Function
async def main():
    device: WiFiDevice = await get_device_by_name()
    if device:
        await connection(device)
        await start_run_program()
        await shutdown()

if __name__ == '__main__' :
    asyncio.run(main())







