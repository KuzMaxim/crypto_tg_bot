from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_reply_keyboard = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Цена конкретной криптовалюты"),
     KeyboardButton(text = "Арбитраж для одной валюты")],
    [KeyboardButton(text = "Мой кошелек"), 
    KeyboardButton(text = "Топ крипты")],
    [KeyboardButton(text = "Регистрация")]
    ], resize_keyboard= True, input_field_placeholder="Выберите необходимую вам функцию")



inline_keyboard_auth = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Войти", callback_data = "log_in")],
    [InlineKeyboardButton(text = "Регистрация", callback_data = "sign_in")],
    [InlineKeyboardButton(text = "Забыл пароль", callback_data = "new_password"),]
    ])


register_button = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "регистрация"), KeyboardButton(text = "главная")]
    ], resize_keyboard = True)