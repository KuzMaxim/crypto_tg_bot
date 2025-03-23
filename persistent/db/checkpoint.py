from .base import Base, uuid4_as_str
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TEXT, TIME, INTEGER


class Session(Base):
    __tablename__ = "checkpoints"
    uuid = Column(TEXT, default = uuid4_as_str(), primary_key = True)
    user_id = Column(TEXT, ForeignKey("users.tgid", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIME)
    session_count = Column(INTEGER, default = 0)
    number = Column(INTEGER, default = 0)
    parent = relationship("users", back_populates="checkpoints")
    