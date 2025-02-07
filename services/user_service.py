from repositories.db.user_repository import UserRepository
import asyncio
from utils.security.salt import generate_salt

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        
    async def put_user(self, tgid:str, nick:str, email:str) -> None:
        uniq_salt = generate_salt()
        return await asyncio.create_task(self.user_repository.put_user(tgid = tgid, nick = nick, email = email, uinq_salt = uniq_salt))
    
    async def get_user(self, tg_id: str) -> str:#gives back token
        return await asyncio.create_task(self.user_repository.get_user(tg_id = tg_id))
    