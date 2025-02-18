import aiohttp
import asyncio
import os

class CoinMarketAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    async def fetch(self, session, relative_url, params=None):
        headers = {"X-CMC_PRO_API_KEY": self.api_key,}
        async with session.get(self.base_url + relative_url, headers=headers, params=params) as response:
            return await response.json()

    async def get_coin(self, ticker: str):
        async with aiohttp.ClientSession() as session:
            params = {"symbol" : ticker,
                      "convert" : "USD"}
            content = await self.fetch(session, "/v2/cryptocurrency/quotes/latest", params = params)
            return str(content["data"][ticker][0]["quote"]["USD"]["price"])
    



    async def get_top_coins(self):
        async with aiohttp.ClientSession() as session:
            content = await self.fetch(session, "/v1/cryptocurrency/listings/latest")
            return content["data"]

