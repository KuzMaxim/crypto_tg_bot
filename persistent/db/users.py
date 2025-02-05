from .base import Base
from sqlalchemy import Column, Text


class User(Base):
    __tablename__ = "users"
    
    tgid = Column(Text, primary_key = True)
    nick = Column(Text, nullable = False)
    email = Column(Text, nullable = False)
    password = Column(Text, nullable = False)
    active = Column(Text, default = "False")