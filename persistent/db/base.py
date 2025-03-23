from sqlalchemy.orm import DeclarativeBase
import uuid


class Base(DeclarativeBase):
    ...
    
    
def uuid4_as_str() -> str:
    return str(uuid.uuid4())