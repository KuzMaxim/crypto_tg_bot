from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv#type:ignore

from presentations.telegram_bot.handlers import router

from repositories.db.top_crypto_repository import crypto_repository
 

load_dotenv()



async def main():
    crypto_repository.check_table()
    bot = Bot(token = os.getenv("TG_BOT_TOKEN"))
    dp =  Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
        

