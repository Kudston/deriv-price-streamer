import asyncio
from src.config import Settings
from redis import Redis
from src.price_feed import subscribe_tick_feed

app_settings = Settings()

async def get_redis_connection():
    return Redis(host=app_settings.redis_host, port=app_settings.redis_port)

if __name__ == "__main__":
    db_store = asyncio.run(get_redis_connection())
    asyncio.run(subscribe_tick_feed(db_store))