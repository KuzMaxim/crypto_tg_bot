import aiohttp
import asyncio
import os

class CryptoService:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    async def fetch(self, session, relative_url, params=None):
        headers = {"X-CMC_PRO_API_KEY": self.api_key,}
        async with session.get(self.base_url + relative_url, headers=headers, params=params) as response:
            return await response.json()

    async def get_coin(self, coin_id: int):
        async with aiohttp.ClientSession() as session:
            params = {"id" : coin_id}
            content = await self.fetch(session, "/v2/cryptocurrency/quotes/latest", params)
            return content["data"]

    async def get_top_coins(self):
        async with aiohttp.ClientSession() as session:
            content = await self.fetch(session, "/v1/cryptocurrency/listings/latest")
            return content["data"]

crypto_service = CryptoService(base_url = "https://pro-api.coinmarketcap.com", api_key = os.getenv("CRYPTO_API_KEY"))
