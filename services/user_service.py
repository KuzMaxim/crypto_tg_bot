from repositories.db.user_repository import UserRepository
import asyncio
from utils.security.salt import Salt

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        
    async def put_user(self, tg_id:str, nick:str, email:str, salt:Salt) -> None:
        return await self.user_repository.put_user(tgid = tg_id, nick = nick, email = email, uniq_salt = salt)
    
    async def get_user(self, tg_id: str) -> str:
        return await self.user_repository.get_user(tg_id = tg_id)
    
    async def get_salt(self, tg_id: str) -> str:
        return await self.user_repository.get_salt(tg_id = tg_id)
    
    async def activate_user(self, tg_id: str) -> None:
        return await self.user_repository.activate(tg_id = tg_id)
    
    async def check_active(self, tg_id: str) -> bool:
        return await self.user_repository.check_active(tg_id = tg_id)
    
    async def get_checkpoints(self, tg_id: str):
        return await self.user_repository.get_checkpoints(tg_id = tg_id)