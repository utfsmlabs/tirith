import sys
import asyncio
import websockets

async def handler():
    async with websockets.connect('ws://localhost:6969') as websocket:
        name = input("> ")
        await websocket.send(name)

        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


def main():
    if args is None:
        args = sys.argv[1:]
    asyncio.get_event_loop().run_until_complete(handler())
    
    print("tirith client 0.1.0-dev0")

if name == "__main__":
    main()
