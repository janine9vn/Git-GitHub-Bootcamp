import asyncio
import os
import sys

loop = asyncio.get_event_loop()


async def main1():
    print("Well, well, well, you seem to have stumbled upon my file...")
    await asyncio.sleep(2)
    print("This is my amazing file that is, wait for it, asynchronous!")
    await asyncio.sleep(1)
    print("Pretty cool right?")


async def main2():
    print(f"What you might not know is, this is currently on python version {sys.version}")
    await asyncio.sleep(1)
    print("Wow!")


async def main3():
    print(f"Another cool thing you might not know, is this is running in the directory: {os.getcwd()}")
    await asyncio.sleep(1)
    print("Fancy, fancy!")


async def main():
    await main1()
    await main2()
    await main3()

loop.run_until_complete(main())
