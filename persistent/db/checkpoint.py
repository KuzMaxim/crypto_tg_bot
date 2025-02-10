from .base import Base, uuid4_as_str
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TEXT


class Session(Base):
    __tablename__ = "checkpoints"
    uuid = Column(TEXT, default = uuid4_as_str(), primary_key = True)
    user_id = Column(TEXT, ForeignKey("users.tgid", ondelete="CASCADE"), nullable=False)
    parent = relationship("users", back_populates="checkpoints")
    