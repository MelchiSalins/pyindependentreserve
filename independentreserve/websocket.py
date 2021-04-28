import websockets
import asyncio
import sys

from pprint import pprint as pp


async def _pull_data(queue: asyncio.Queue):
    async with websockets.connect(WSS_URL) as websocket:
        while True:
            data = await websocket.recv()
            data = data.encode("utf-8")
            await queue.put(data)


# def subscribe(conf: IRWSSConfig = None) -> None:
async def wss_subscribe(queue: asyncio.Queue, channel_name: list = ["ticker-xbt-aud"]):
    try:
        if len(channel_name) > 1:
            channel = ",".join(channel_name)
        else:
            channel = channel_name[0]
        WSS_URL = f"wss://websockets.independentreserve.com?subscribe={channel}"
        async with websockets.connect(WSS_URL) as websocket:
            while True:
                data = await websocket.recv()
                data = data.encode("utf-8")
                await queue.put(data)
    except Exception as error:
        print(error)
        sys.exit(1)
