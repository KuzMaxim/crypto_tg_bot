from infrastructure.sql.connect import create_connection, create_tables
from persistent.db.checkpoint import Session
from sqlalchemy import select, insert, update


class SessionRepository:
    def __init__(self):
        self.sessionmaker = create_connection()
        create_tables()
    
    async def make_checkpoint(self, tgid:str, nick:str, email:str, uniq_salt:str) -> None:

        stmp = insert(Session).values({})
        
        async with self.sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
    