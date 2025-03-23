from .base import Base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT


class User(Base):
    __tablename__ = "users"
    
    tgid = Column(TEXT, primary_key = True)
    nick = Column(TEXT, nullable = False)
    email = Column(TEXT, nullable = False)
    salt = Column(TEXT, nullable = False, default = ("0" * 16))
    active = Column(TEXT, default = "False")