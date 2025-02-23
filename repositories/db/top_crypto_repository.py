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

    def get_top_crypto(self) -> dict:
        print("get_top_crypto_repository")
        try:
            keys = self.repository.keys('*')
        except redis.ConnectionError as e:
            print(f"Ошибка подключения: {e}")
            return {}

        data_dict = {}
        
        
        for key in keys:
            value = self.repository.get(key)
            data_dict[key.decode('utf-8')] = value.decode('utf-8') if value else None

        return data_dict
    
    def update(self):
        print("update_crypto")
        new_data = self.coin_market_API.get_top_coins_synch()
        if new_data:
            self.repository.flushdb()
            self.repository.mset(new_data)
    
    def check_table(self):
        print("check_table")
        with open("repositories/db/logs/Redis/top_crypto.txt", "w") as logs:

            keys = self.repository.keys('*')

            for key in keys:
                value = self.repository.get(key)
                logs.write(f"{key} : {value}\n")
    
    
    def schedule_update(self):
        print("schedule_update_crypto")   
        update_times = ["08:00", "12:00", "16:00", "20:00"]

        gmt = pytz.timezone('GMT')

        for time_str in update_times:
            schedule.every().day.at(time_str).do(self.update)

        while True:
            schedule.run_pending()
            time.sleep(50)



crypto_repository = CryptoRepository(host=os.getenv("DB_HOST_REDIS"), port=os.getenv("DB_PORT_REDIS_USERS"), db = 0)#username = os.getenv("DB_NAME_REDIS"), password = os.getenv("DB_PASS_REDIS"), db = 0)
        