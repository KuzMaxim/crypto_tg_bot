import redis#type:ignore
from dotenv import load_dotenv#type:ignore
import os
import schedule#type:ignore
import pytz
import threading
import time
import asyncio
from utils.API.coinmarketcap import CoinMarketAPI

load_dotenv()


    
    
class CryptoRepository:
    
    def __init__(self, host, port, db):
        self.repository = redis.StrictRedis(host = host, port = port, db = db)
        scheduler_thread = threading.Thread(target = self.schedule_update)
        scheduler_thread.daemon = True
        self.coin_market_API = CoinMarketAPI()
        scheduler_thread.start()

    async def get_top_crypto(self) -> dict:
        keys = self.repository.keys('*')

        data_dict = {}

        for key in keys:
            value = self.repository.get(key)
            data_dict[key.decode('utf-8')] = value.decode('utf-8') if value else None

        return data_dict
    
    def update(self):
        new_data = self.coin_market_API.get_top_coins_synch()
        if new_data:
            self.repository.flushdb()
            self.repository.mset(new_data)
    
    def check_table(self):
        
        with open("repositories/db/logs/Redis.txt", "w") as logs:

            keys = self.repository.keys('*')

            for key in keys:
                value = self.repository.get(key)
                logs.write(f"{key} : {value}\n")
        
    def schedule_update(self):   
        update_times = ["08:00", "12:00", "16:00", "20:00"]

        gmt = pytz.timezone('GMT')

        for time_str in update_times:
            schedule.every().day.at(time_str).do(self.update)

        while True:
            schedule.run_pending()
            time.sleep(50)

crypto_repository = CryptoRepository(host = os.getenv("DB_HOST_REDIS"), port = os.getenv("DB_PORT_REDIS"), db = 0)# username = os.getenv("DB_USER_REDIS"), password = os.getenv("DB_PASS_REDIS"),


