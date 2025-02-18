import redis#type:ignore
from dotenv import load_dotenv#type:ignore
import os
import schedule#type:ignore
import pytz
import threading
import time
load_dotenv()



class CryptoRepository:
    
    
    def __init__(self, host, port, db):
        self.repository = redis.StrictRedis(host = host, port = port, db = db)
        scheduler_thread = threading.Thread(target = self.schedule_jobs)
        scheduler_thread.daemon = True
        scheduler_thread.start()

    def update(self):
        ...
    def schedule_jobs(self):   
        update_times = ["08:00", "12:00", "16:00", "20:00"]

        gmt = pytz.timezone('GMT')

        for time_str in update_times:
            schedule.every().day.at(time_str).do(self.update)

        while True:
            schedule.run_pending()
            time.sleep(50)


crypto_repository = CryptoRepository(host = os.getenv("DB_HOST_REDIS"), port = os.getenv("DB_PORT_REDIS"), db = 0)# username = os.getenv("DB_USER_REDIS"), password = os.getenv("DB_PASS_REDIS"),


