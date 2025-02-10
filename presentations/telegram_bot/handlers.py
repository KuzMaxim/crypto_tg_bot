from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from services.user_service import UserService
from utils.email.confirming_email import send_email
from presentations.telegram_bot.keyboards import *
from utils.security.salt import generate_salt


class Register(StatesGroup):
    nick = State()
    tg_id = State()
    email_reg = State()
    check_email = State()
    finish_reg = State()
    waiting = State()
    confirmed = State()
    reg_started = State()
    
class User(StatesGroup):
    admin = State()
    authorised = State()
    unauthorised = State()
    

router = Router()
bot_user_service = UserService()
number_for_confirming = ""

@router.message(F.text.upper().in_({"ГЛАВНАЯ", "MAIN", "/START", "МЕНЮ"}))
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

    
    
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Так, тебе нужна помощь! Я этот раздел пока не сделал, так что попробуй, пожалуйста, разобраться самостоятельно")

     
@router.message(F.text.upper() == "РЕГИСТРАЦИЯ")
async def register(message:Message, state: FSMContext):
    print(await state.get_state())
    await state.set_state(Register.nick)
    await state.update_data(tg_id  = message.from_user.id)
    await message.answer("Как мне к тебе обращаться?")


@router.message(Register.nick)
async def reg_email(message: Message, state: FSMContext):
    await state.update_data(nick = message.text)
    await state.set_state(Register.email_reg)
    await message.answer(
"""Удобная тебе действительная почта
Образец: my_email@gmail.com"""
    )
    
    

@router.message(Register.email_reg)
async def reg_password(message: Message, state: FSMContext):
    await state.update_data(reg_email = message.text)
    data = await state.get_data()
    gen_salt = generate_salt()
    await bot_user_service.put_user(email = data["reg_email"], nick = data["nick"], tgid = data["tg_id"], salt = gen_salt)
    if str(await send_email(getter = message.text, tg_id = data["tg_id"])) == "Message was not sent":
        await message.answer("Сообщение не получилось отправить")
        await state.clear()
    else:
        await message.answer("Перейди по ссылке, отправленной на указанную почту")
        await state.set_state(Register.waiting)
    

@router.message(Register.waiting)
async def confirming_email(message:Message, state: FSMContext):
    if message.text ==  number_for_confirming:
        await message.answer(f"Регистрация прошла успешно")
    else:
        await message.answer("Введенное число не совпало с отправленным(. Но ты всегда можешь начать процесс ргеистрации заново!")
    await state.clear()