import json
import asyncio
from websockets.client import connect
from redis import Redis
from src.config import Settings

app_settings = Settings()

async def subscribe_tick_feed(db_store: Redis):
    async with connect('wss://api.derivws.com/trading/v1/options/ws/public') as ws:
        request = {
            "ticks":"BOOM1000",
            "subscribe":1
        }
        await ws.send(json.dumps(request))

        while True:
            response = await ws.recv()
            payload = json.loads(response)
            # Redis Streams require a flat field->value map; store raw JSON string.
            db_store.xadd(app_settings.tick_data_key, {"payload": response})
