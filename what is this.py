import asyncio
import os
import sys

loop = asyncio.get_event_loop()


async def main():
    print("Well, well, well, you seem to have stumbled upon my file...")
    await asyncio.sleep(2)
    print("This is my amazing file that is, wait for it, asynchronous!")
    await asyncio.sleep(1)
    print("Pretty cool right?")


async def version():
    print(f"What you might not know is, this is currently on python version {sys.version}")
    await asyncio.sleep(1)
    print("Wow!")


async def directory():
    print(f"Another cool thing you might not know, is this is running in the directory: {os.getcwd()}")
    await asyncio.sleep(1)
    print("Fancy, fancy!")

list(map(loop.create_task, [main(), version(), directory()]))
