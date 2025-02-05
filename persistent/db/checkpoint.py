from base import Base, uuid4_as_str
from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.orm import relationship


class Session(Base):
    __tablename__ = "checkpoints"
    uuid = Column(Text, default = uuid4_as_str())
    user_id = Column(Text, ForeignKey("users.tgid"), ondelete = "CASCADE", nullable = False)
    parent = relationship()
    