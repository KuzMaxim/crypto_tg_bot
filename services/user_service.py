from repositories.db.user_repository import UserRepository
import asyncio

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        
    async def put_user(self, tgid:str, nick:str, email:str, pswd:str) -> None:
        return await asyncio.create_task(self.user_repository.put_user(tgid = tgid, nick = nick, email = email, pswd = pswd))
    
    async def get_user(self, email:str, pswd: str) -> str:#gives back token
        return await asyncio.create_task(self.user_repository.get_user(email = email, pswd = pswd))
    