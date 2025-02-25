from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_reply_keyboard = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Цена конкретной криптовалюты"),
     KeyboardButton(text = "Арбитраж для одной валюты")],
    [KeyboardButton(text = "Мой кошелек"), 
    KeyboardButton(text = "Топ крипты")],
    [KeyboardButton(text = "Регистрация")]
    ], resize_keyboard= True, input_field_placeholder="Выберите необходимую вам функцию")



inline_keyboard_wallet = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Посмотреть кошелек", callback_data = "check_wallet")],
    [InlineKeyboardButton(text = "Поменять кошелек", callback_data = "change_wallet")],
    ])


register_button = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "регистрация"), KeyboardButton(text = "главная")]
    ], resize_keyboard = True)