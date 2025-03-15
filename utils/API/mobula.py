import aiohttp
import asyncio
from dotenv import load_dotenv#type: ignore
import os

load_dotenv()

class MobulaAPI:
    def __init__(self):
        self.base_url = "https://api.mobula.com/"
        self.api_key = os.getenv("MOBULA_API_KEY")

    async def fetch(self, session, relative_url, ticker: str, params = None):
        headers = {
        'Authorization': self.api_key,
        'Token-Symbol': ticker.upper()
    }
        async with session.get(self.base_url + relative_url, headers=headers, params = params) as response:
            return await response.json()

    async def get_coin(self, ticker: str) -> str:#gives back price in USDT
        async with aiohttp.ClientSession() as session:
            content = await self.fetch(session, "/v2/cryptocurrency/quotes/latest", ticker = ticker)
            return str(content["price"])
