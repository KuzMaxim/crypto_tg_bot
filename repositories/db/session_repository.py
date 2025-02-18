from infrastructure.sql.connect import create_connection, create_tables
from persistent.db.checkpoint import Session
from sqlalchemy import select, insert, update

class SessionRepository:
    def __init__(self):
        self.sessionmaker = create_connection()
        create_tables()
    
    