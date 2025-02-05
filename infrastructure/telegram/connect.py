from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv#type:ignore

from .handlers import router
 

load_dotenv()



async def main():
    bot = Bot(token = os.getenv("TG_BOT_TOKEN"))
    dp =  Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)#начинаем обращаться к серверу телеграм за обновлениями
        

