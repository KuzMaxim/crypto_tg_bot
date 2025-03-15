import aiohttp
from dotenv import load_dotenv#type: ignore
import requests
import asyncio
import os

load_dotenv()

class CoinMarketAPI:
    def __init__(self) -> dict:
        self.base_url = "https://pro-api.coinmarketcap.com"
        self.api_key = os.getenv("CRYPTO_API_KEY")

    async def fetch(self, session, relative_url, params=None):
        headers = {"X-CMC_PRO_API_KEY": self.api_key,}
        async with session.get(self.base_url + relative_url, headers=headers, params=params) as response:
            return await response.json()

    async def get_coin(self, ticker: str) -> str:
        async with aiohttp.ClientSession() as session:
            params = {"symbol" : ticker.upper(),
                      "convert" : "USD"}
            content = await self.fetch(session, "/v2/cryptocurrency/quotes/latest", params = params)
            return str(content["data"][ticker.upper()][0]["quote"]["USD"]["price"])
    

    async def get_top_coins(self) -> list:
        async with aiohttp.ClientSession() as session:
            params = {'start': '1',
                    'limit': '100',
                    'convert': 'USD'}
            content = await self.fetch(session, "/v1/cryptocurrency/listings/latest")
            return content["data"]
        
        
    def get_top_coins_synch(self) -> dict:
        try:
            response = requests.get(self.base_url + "/v1/cryptocurrency/listings/latest", headers ={"X-CMC_PRO_API_KEY": self.api_key})
            response.raise_for_status()
            data = response.json()
            data_dict = {}
            
            for crypto in data["data"]:
                name = crypto['name']
                price = crypto['quote']['USD']['price']
                data_dict[name] = price
                
            return data_dict
        except:
            raise Exception
