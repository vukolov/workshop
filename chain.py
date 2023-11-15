import asyncio
from websockets.server import serve
from websockets.sync.client import connect

def send(msg):
    with connect("ws://localhost:42070") as websocket:
        websocket.send(msg)
        return websocket.recv()
async def echo(websocket):
    async for message in websocket:
        result = send(message)
        await websocket.send(result)

async def main():
    async with serve(echo, "localhost", 42069):
        await asyncio.Future()  # run forever

asyncio.run(main())
