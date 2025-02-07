from hashlib import sha256
import os
from dotenv import load_dotenv#type:ignore


load_dotenv()

def create_hash_pswd(pswd:str) -> str:
    hash_pswd = sha256()
    pswd = pswd + os.getenv("SALT")
    hash_pswd.update(pswd.encode())
    hash_pswd = str(hash_pswd.hexdigest())
    return hash_pswd