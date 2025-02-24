from infrastructure.sql.connect import create_connection, create_tables
from persistent.db.users import User
from sqlalchemy import select, insert, update


class UserRepository:
    def __init__(self):
        self.sessionmaker = create_connection()
        create_tables()
    
    async def put_user(self, tgid:str, nick:str, email:str, uniq_salt:str) -> None:

        stmp = insert(User).values({"tgid":tgid, "email":email, "nick":nick, "active": "True", "salt":uniq_salt})
        
        async with self.sessionmaker() as session:
            await session.execute(stmp)
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
        stmp = select(User.checkpoint).where(User.tgid == tg_id)
        
        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchall()
        if row is None:
            return None
        else:
            return row
        