import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        await websocket.send(name)

        accepted = await websocket.recv()
        target = input(f"< {accepted}") #

        await websocket.send(target)
        #message = input()

        messageRequest = await websocket.recv()
        message = input(f" \
            {messageRequest}"
            )
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(hello())
