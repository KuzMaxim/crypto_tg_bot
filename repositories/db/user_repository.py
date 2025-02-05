from infrastructure.sql.connect import create_connection, create_tables
from persistent.db.users import User
from sqlalchemy import select, insert
from utils.security.pswd_hash import create_hash_pswd


class UserRepository:
    def __init__(self):
        self.sessionmaker = create_connection()
        create_tables()
    
    async def put_user(self, tgid:str, nick:str, email:str, pswd:str) -> None:
        hash_pswd = create_hash_pswd(pswd)

        stmp = insert(User).values({"tgid":tgid, "email":email, "nick":nick, "active": "True", "password":hash_pswd})
        
        async with self.sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
    
    async def get_user(self, email:str, pswd:str):
        hash_pswd = create_hash_pswd(pswd)
        
        stmp = select(User.tgid).where(User.password == hash_pswd, User.email == email).limit(1)
            
        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchone()
        if row is None:
            return None
        else:
            return row[0]
