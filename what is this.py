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
