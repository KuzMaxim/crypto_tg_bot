from utils.API.coinmarketcap import CoinMarketAPI
import asyncio
from dotenv import load_dotenv#type:ignore
import os

load_dotenv()

api = CoinMarketAPI()


class CryptoService:
    async def get_specific_crypto(self, ticker : str):
        return await api.get_coin(ticker = ticker)