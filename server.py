import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        message = 'bla-bla-' + message
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 42070):
        await asyncio.Future()  # run forever

asyncio.run(main())
