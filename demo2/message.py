import asyncio
import websockets

async def hello(websocket, path):
    users = []
    user = await websocket.recv()
    print(f"< {user}")
    users.append(user)

    greeting = f"Hello {user}! Who do you wish to speak with? "

    await websocket.send(greeting)
    print(f"> {greeting}")

    messagePair = {}
    target = await websocket.recv()
    messagePair = {user:target}
    await websocket.send(f" \
        You are connected with {target}! \
        What do you wish to say? \
        ")
    msg = await websocket.recv()
    print(msg)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
