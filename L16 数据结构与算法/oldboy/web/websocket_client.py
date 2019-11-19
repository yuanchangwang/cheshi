# coding=utf-8
"""
author = jamon
"""

import websockets
import asyncio


async def hello_client():
    async with websockets.connect("ws://localhost:8888") as websocket:
        name = input("what's your name? ")
        await websocket.send(name)
        print("send server: ", name)
        greeting = await websocket.recv()
        print("receive from server: ", greeting)

asyncio.get_event_loop().run_until_complete(hello_client())