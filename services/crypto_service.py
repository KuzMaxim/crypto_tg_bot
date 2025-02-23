from utils.API.coinmarketcap import CoinMarketAPI
from utils.API.binance import BinanceAPI
from utils.API.poloniex import PoloniexAPI
import asyncio
from repositories.db.top_crypto_repository import crypto_repository
from dotenv import load_dotenv#type:ignore


class CryptoService:
    def __init__(self):
        self.top_crypto_repository = crypto_repository
        self.coin_market_api = CoinMarketAPI()
        self.poloniex_api = PoloniexAPI()
        self.binance_api = BinanceAPI()

    async def get_specific_crypto(self, ticker : str) -> dict:#gives back price in USD(using all API)
        async with asyncio.TaskGroup() as tg:
            self.coin_market = tg.create_task(self.coin_market_api.get_coin(ticker = ticker))
            self.poloniex = tg.create_task(self.poloniex_api.get_coin(ticker = ticker))
            self.binance = tg.create_task(self.binance_api.get_coin(ticker = ticker))
        return {"coin_market" : await self.coin_market, "poloniex" : await self.poloniex, "binance" : await self.binance}
    
    async def get_top_crypto(self) -> dict:
        return await self.top_crypto_repository.get_top_crypto()
    
    async def compare_price_specific_crypto(self, ticker : str) -> list:
        raw_data = await self.get_specific_crypto(ticker = ticker)
        data = list(raw_data.items())
        data.sort(key = lambda x : x[-1], reverse = True)
        return data
            