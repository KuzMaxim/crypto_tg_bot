from .base import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TEXT
from .checkpoint import Checkpoint


class User(Base):
    __tablename__ = "users"
    
    tgid = Column(TEXT, primary_key = True)
    nick = Column(TEXT, nullable = False)
    email = Column(TEXT, nullable = False)
    salt = Column(TEXT, nullable = False, default = ("0" * 16))
    active = Column(TEXT, default = "False")
    checkpoint = relationship("Checkpoint", uselist=False, back_populates="user")