# coding=utf-8
"""
author = jamon
"""

import websockets
import asyncio


async def hello(websocket, path):
    name = await websocket.recv()
    print("a new client: ", name)
    greeting = "welcome " + name
    await websocket.send(greeting)
    print("send ", greeting, " to ", name)

start_server = websockets.serve(hello, "localhost", 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()