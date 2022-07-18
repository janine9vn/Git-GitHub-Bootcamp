import asyncio
import os
import sys

loop = asyncio.get_event_loop()


'''
Coroutine main

It just... Does the thing
No args -> None
'''
async def main() -> None:
    print("Well, well, well, you seem to have stumbled upon my file...")
    await asyncio.sleep(2)
    print("This is my amazing file that is, wait for it, asynchronous!")
    await asyncio.sleep(1)
    print("Pretty cool right?")


'''
Coroutine version

It prints the system version
No args -> None
'''
async def version() -> None:
    print(f"What you might not know is, this is currently on python version {sys.version}")
    await asyncio.sleep(1)
    print("Wow!")



'''
Coroutine directory

It prints the current working directory
No args -> None
'''
async def directory() -> None:
    print(f"Another cool thing you might not know, is this is running in the directory: {os.getcwd()}")
    await asyncio.sleep(1)
    print("Fancy, fancy!")


'''
This is meant to map the task wrapper over each coro, ik I could just do this as @deco over the async funcs but, you know, I'm bored
'''
list(map(loop.create_task, [main(), version(), directory()]))

'This does nothing'
None
'LOL'
