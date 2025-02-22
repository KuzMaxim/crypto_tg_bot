import aiohttp
from dotenv import load_dotenv#type: ignore
import os

load_dotenv()


class MobulaAPI:
    def __init__(self):
        self.base_url = "https://futures-api.poloniex.com"

    async def fetch(self, session, relative_url, params = None):
        headers = {}
        async with session.get(self.base_url + relative_url, headers=headers, params = params) as response:
            return await response.json()

    async def get_coin(self, ticker: str) -> str:#gives back price in USDT
        async with aiohttp.ClientSession() as session:
            params = ticker.upper()
            content = await self.fetch(session, f"/api/v1/contracts/{params}USDTPERP")
            return str(content["data"]["lastTradePrice"])
