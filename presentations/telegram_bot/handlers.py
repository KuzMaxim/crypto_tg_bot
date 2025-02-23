from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from services.user_service import UserService
from utils.email.confirming_email import send_email
from presentations.telegram_bot.keyboards import *
from utils.security.salt import generate_salt
import asyncio
from services.crypto_service import CryptoService

class Register(StatesGroup):
    nick = State()
    tg_id = State()
    email_reg = State()
    check_email = State()
    active = State()
    reg_started = State()
    waiting = State()

class CoinPrice(StatesGroup):
    ticker = State()

class ComparingPrice(StatesGroup):
    ticker = State()
    
    
crypto_service = CryptoService()
router = Router()
bot_user_service = UserService()


@router.message(F.text.upper().in_({"ГЛАВНАЯ", "MAIN", "МЕНЮ", "/START"}))
async def cmd_start(message: Message):
    await message.answer(
"""Привет, я создан для помощи в ведении твоего криптокошелька.
Какой функционал я предоставляю:
1)ты можешь видеть изменения в цене какой-то конкретной крипты, а также получать информацию о самых интересных изменениях на бирже за последнее время\n
2)ты можешь создавать "контрольные точки". В них я буду фиксировать твое количество той или иной валюты, а также актуальную на тот момент цену, впослеждствии ты сможешь сравнивать свое текущее положение дел с "контрольными точками" и видеть, как изменилась отдельная крипта или портфель в целом
Важные особенности:
Я не предоставляю доступа к каким-либо коммерческим операциям, выполняя роль удобной утилиты для хранения информации, у меня не будет доступа к твоим персональным данным(кроме почты и ника, который ты волен выбирать сам) и финансовым инструментам
Прости за долгое вступление) Давай же познакомимся!""", reply_markup = start_reply_keyboard
                         )

@router.message(F.text.upper() == "ТОП КРИПТЫ")
async def give_top_crypto(message: Message):
    data_dict = crypto_service.get_top_crypto()
    answer_str = str()
    for key in data_dict:
        answer_str += f"{key} : {data_dict[key]}\n"
    await message.answer(answer_str)
    

# @router.message(F.text.upper() == "МОЙ КОШЕЛЕК")
# async def check_wallet(message: Message):
#     top_crypto_sesrvice.add_crypto("FIRST FUNC", "STILL 1ST")
#     top_crypto_sesrvice.get_crypto("FIRST FUNC")

@router.message(F.text.upper() == "АРБИТРАЖ ДЛЯ ОДНОЙ ВАЛЮТЫ")
async def compare_price_specific_crypto_ticker(message: Message, state: FSMContext):
    if bot_user_service.check_active_user(tg_id = str(message.from_user.id)):
        async def func():
            async with asyncio.TaskGroup() as tg:
                tg.create_task(state.set_state(ComparingPrice.ticker))
                tg.create_task(message.answer("Напишите тикер(сокращенное название) нужной вам криптовалюты(например, BTC)"))
        return await func()
    else:
        async def func():
            async with asyncio.TaskGroup() as tg:
                tg.create_task(state.clear())
                tg.create_task(message.answer("Зарегистрируйтесь для использования этой функции"))
        return await func()


@router.message(ComparingPrice.ticker)
async def compare_price_specific_crypto(message: Message, state: FSMContext):
    crypto = await crypto_service.compare_price_specific_crypto(ticker = message.text)
    async def func():
        async with asyncio.TaskGroup() as tg:
            tg.create_task(await message.answer(f"Самая выгодная цена = {round(float(crypto[0][1]), 5)}, самая низкая цена = {round(float(crypto[-1][1]), 5)}, потенциальная выгода = {round(float(crypto[0][1]) - float(crypto[-1][1]), 5)}"))
            tg.create_task(state.clear())
    return await func()
    
    
@router.message(F.text.upper() == "ЦЕНА КОНКРЕТНОЙ КРИПТОВАЛЮТЫ")
async def get_price_specific_crypto_ticker(message: Message, state: FSMContext):
    await state.set_state(CoinPrice.ticker)
    await message.answer("Напишите тикер(сокращенное название) нужной вам криптовалюты(например, BTC)")


@router.message(CoinPrice.ticker)
async def get_price_specific_crypto(message: Message, state: FSMContext):
    price = await crypto_service.get_specific_crypto(ticker = message.text)
    await message.answer(str(round(float(price["binance"]), 5)) + "$ (USD)")
    await state.clear()
    
    
    
@router.message(Command('help'))
async def cmd_help(message: Message):
    async with asyncio.TaskGroup() as tg:
        tg.create_task(message.answer("Так, тебе нужна помощь! Я этот раздел пока не сделал, так что попробуй, пожалуйста, разобраться самостоятельно"))

     
@router.message(F.text.upper().in_({"РЕГИСТРАЦИЯ", "ЗАРЕГИСТРИРОВАТЬСЯ", "/REGISTER", "REGISTER"}))
async def register(message:Message, state: FSMContext):
    async with asyncio.TaskGroup() as tg:
        data = await state.get_data()
        try:
            if data["active"] == "True":
                tg.create_task(message.answer("Вы уже зарегистрированы"))
        except Exception:     
            tg.create_task(state.set_state(Register.nick))
            tg.create_task(state.update_data(tg_id  = str(message.from_user.id)))
            await message.answer("Как мне к тебе обращаться?")


@router.message(Register.nick)
async def reg_email(message: Message, state: FSMContext):
    async with asyncio.TaskGroup() as tg:
        tg.create_task(state.update_data(nick = message.text))
        tg.create_task(state.set_state(Register.email_reg))
        await message.answer(
"""Удобная тебе действительная почта
Образец: my_email@gmail.com"""
    )
    
    

@router.message(Register.email_reg)
async def reg_password(message: Message, state: FSMContext):
    async with asyncio.TaskGroup() as tg:
        await state.update_data(reg_email = message.text)
        data = await state.get_data()
        gen_salt = generate_salt()
        await bot_user_service.put_user(email = data["reg_email"], nick = data["nick"], tg_id = data["tg_id"], salt = gen_salt)
        if str(await tg.create_task(send_email(getter = message.text, salt = gen_salt))) == "Message was not sent":
            await message.answer("Сообщение не получилось отправить")
            tg.create_task(state.clear())
        else:
            await message.answer("Перейди по ссылке, отправленной на указанную почту")
            tg.create_task(state.set_state(Register.waiting))
    

@router.message(Register.waiting)
async def start_function(message:Message, state:FSMContext):
    async with asyncio.TaskGroup() as tg:
        data = await state.get_data()
        salt = message.text
        if salt == await bot_user_service.get_salt(tg_id = data["tg_id"]):
            tg.create_task(bot_user_service.activate_user(tg_id = data["tg_id"]))
            tg.create_task(state.update_data(active = "True"))
            await message.answer("Вы успешно зарегистрированы и ваш аккаунт активирован! 🎉")
        else:
            await message.answer("Что-то пошло не так, но вы можете начать регистрацию заново")
        tg.create_task(state.clear())