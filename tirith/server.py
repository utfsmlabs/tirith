import sys
import asyncio
import websockets

clients = set()
async def handler(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            clients.add(websocket.remote_address[0])
            print(','.join(clients))
        except websockets.exceptions.ConnectionClosed:
            print("connection closed")
            clients.remove(websocket.remote_address[0])
            break
    print(','.join(clients))


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("tirith server is listening...")
    start_server = websockets.serve(handler, 'localhost', 6969)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
