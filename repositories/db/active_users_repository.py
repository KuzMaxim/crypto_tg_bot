import redis#type: ignore
from dotenv import load_dotenv#type:ignore
import os


load_dotenv()


    
    
class ActiveUserRepository:
    def __init__(self, host, port, db):
        self.repository = redis.StrictRedis(host = host, port = port, db = db)

    def check_table(self) -> dict:
        print("check_table_user")
        keys = self.repository.keys('*')

        data = {}
        
        for key in keys:
            data[key] = self.repository.get(key)
            
        with open("repositories/db/logs/Redis/active_users.txt", "w") as logs:
            for key in keys:
                    logs.write(f"{key} : {data[key]}\n")      
        
    
    def check_user(self, tg_id: str) -> bool:
        print("check_user")
        key = tg_id
        
        if self.repository.get(key):
            return True
        else: 
            return False
    
active_user_repository = ActiveUserRepository(host=os.getenv("DB_HOST_REDIS"), port=os.getenv("DB_PORT_REDIS_USERS"), db = 0)#username = os.getenv("DB_NAME_REDIS"), password = os.getenv("DB_PASS_REDIS"),
        