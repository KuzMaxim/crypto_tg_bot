from infrastructure.sql.connect import create_connection, create_tables
from persistent.db.users import User, Checkpoint
from sqlalchemy import select, insert, update
from datetime import datetime
from sqlalchemy.dialects.postgresql import INTEGER
import asyncio

class UserRepository:
    def __init__(self):
        self.sessionmaker = create_connection()
        create_tables()
    
    async def put_user(self, tgid:str, nick:str, email:str, uniq_salt:str) -> None:

        time = str(datetime.now())
        stmp = insert(User).values({"tgid":tgid, "email":email, "nick":nick, "active": "True", "salt":uniq_salt})
        stmp2 = insert(Checkpoint).values({"user_id":tgid, "created_at":time})
        
        
        async with self.sessionmaker() as session:
            async with asyncio.TaskGroup() as tg:
                await session.execute(stmp)
                await session.execute(stmp2)
                
            
            await session.commit()
    
    async def get_user(self, tg_id: str):
        
        stmp = select(User.nick).where(User.tgid == tg_id).limit(1)
            
        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchone()
        if row is None:
            return None
        else:
            return row[0]
        
    async def get_salt(self, tg_id: str):
        
        stmp = select(User.salt).where(User.tgid == tg_id).limit(1)
            
        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchone()
        if row is None:
            return None
        else:
            return row[0]
        
    async def activate(self, tg_id: str):
        stmp = update(User).where(User.tgid == tg_id).values(active="True")
        
        async with self.sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
    
    async def check_active(self, tg_id: str) -> bool:
        stmp = select(User.active).where(User.tgid == tg_id)
        
        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchone()
        if row is None:
            return None
        else:
            return bool(row[0])
    
    async def get_checkpoints(self, tg_id: str):
        stmp = select(Checkpoint).join(User).where(User.tgid == str(tg_id))
        
        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchall()
        if row is None:
            return None
        else:
            return row[0][0].created_at
        