import os
import binascii
from pydantic import BaseModel, constr

def generate_salt():
    salt = os.urandom(16)
    return binascii.hexlify(salt).decode('utf-8')


class Salt(BaseModel):
    uniq_salt : constr(max_length = 16, min_length = 16)
