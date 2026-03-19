import json
import asyncio
import pandas as pd
from websockets.client import connect
from src.config import Settings

app_settings = Settings()

async def get_symbols():
    async with connect('wss://api.derivws.com/trading/v1/options/ws/public') as ws:
        request = {
            'active_symbols':'brief',
        }
        await ws.send(json.dumps(request))

        while True:
            response = await ws.recv()
            response = json.loads(response)
            return response

def get_save_symbols():
    result = asyncio.run(get_symbols())
    try:
        df = pd.DataFrame(result['active_symbols'])
        df.to_csv(app_settings.symbols_save_file)
        print("Data saved succesfully to {0}".format(app_settings.symbols_save_file))
    except Exception as e:
        print("Data recieved is incorrect.")
        raise e
