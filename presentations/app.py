import fastapi
from services.user_service import UserService
from services.crypto_service import CryptoService
import asyncio


app = fastapi.FastAPI(title = "PetProject")

user_service = UserService()


# @app.get("/home")
# async def home_page():
#     return("That's home page!")

# @app.post("/registration")
# async def registrate(tgid:str, nick:str, email:str, pswd:str) -> None:
#     result = await asyncio.create_task(user_service.put_user(tgid = tgid, nick = nick, email = email, pswd = pswd))
    
# @app.get("/get_token")
# async def get_token(email:str, pswd: str) -> str:
#     result = await asyncio.create_task(user_service.get_user(email = email, pswd = pswd))
#     return result

# @app.get("/get_specific_crypto")
# async def get_specific_crypto(id : int): #-> str:
#     result = await asyncio.create_task(crypto_service.get_coin(id))
#     return result

# @app.get("/get_top_crypto")
# async def get_top_crypto():# -> str:
#     result = await asyncio.create_task(crypto_service.get_top_coins())
#     return result