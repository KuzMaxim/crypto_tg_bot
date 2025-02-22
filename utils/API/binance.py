import aiohttp

class BinanceAPI:
    def __init__(self):
        self.base_url = "https://api.binance.com"

    async def fetch(self, session, relative_url, params=None):
        async with session.get(self.base_url + relative_url, params=params) as response:
            return await response.json()

    async def get_coin(self, ticker: str) -> str:#gives back price in USDT
        async with aiohttp.ClientSession() as session:
            params = {"symbol" : ticker + "USDT",
                      }
            content = await self.fetch(session, "/v2/cryptocurrency/quotes/latest", params = params)
            return str(content["price"])
