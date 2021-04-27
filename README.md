# pyindependentreserve
Python client for Interacting with Independent Reserve API - The Bitcoin and Digital Currency Market

# Install 
```bash
$ pip install pyindependentreserve
```


# Usage REST API
```python
$ python
>>> import independentreserve as ir
>>> connection = ir.PublicMethods()
>>> connection.get_valid_limit_order_types()
[u'LimitBid', u'LimitOffer'] 

>>> api = PrivateMethods("your_api_key", "your_api_secret")
>>> api.get_open_orders()
{'TotalItems': ... etc
```

# Usage Websocket
pyindependentreserve uses python3 asyncio module to implement a producer consumer pattern to consume messages from the websocket. 

Official websocket documentation can be found here: https://github.com/independentreserve/websockets
```python
from asyncio.queues import Queue
import websockets
import asyncio
import sys

from independentreserve import wss_subscribe


async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print("consuming item: {}".format(item))


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        queue = asyncio.Queue(1000)
        producer_coroutine = wss_subscribe(queue=queue, channel_name=["ticker-xbt-aud"])
        consumer_coroutine = consumer(queue=queue)
        loop.run_until_complete(asyncio.gather(producer_coroutine, consumer_coroutine))
        loop.close()
    except Exception as error:
        print(error)
        sys.exit(1)
```

# Support

If you like this project and would want to support it please consider taking a look
at the issues section at:

https://github.com/MelchiSalins/pyindependentreserve/issues

or consider donating to

Bitcoin:  1B2kZETHm9tjhPKtCCEo6eWhwT5TfXWE6u
Etherium: 0x00912fdef62ab7d9c1cbee712a58105eb1dbd42f
BitCash:  1B2kZETHm9tjhPKtCCEo6eWhwT5TfXWE6u