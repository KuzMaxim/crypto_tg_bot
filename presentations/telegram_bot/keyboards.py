from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_reply_keyboard = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Вход/Регистрация/Восстановление пароля")],
    [KeyboardButton(text = "Запись на занятия"), KeyboardButton(text = "Просмотр имеющихся записей")], 
    [KeyboardButton(text = "Резензии на книги автора в NewYorkPost (не шутка, просто играюсь с API) (пример ввода: Stephen King)")],
    ], resize_keyboard= True, input_field_placeholder="Выбери чонить по-братски")



inline_keyboard_auth = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Войти", callback_data = "log_in")],
    [InlineKeyboardButton(text = "Регистрация", callback_data = "sign_in")],
    [InlineKeyboardButton(text = "Забыл пароль", callback_data = "new_password"),]
    ])


inline_keyboard_log_in_users = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Студент", callback_data = "student")],
    [InlineKeyboardButton(text = "Преподаватель", callback_data = "teacher")],
    [InlineKeyboardButton(text = "Да я так, по приколу, салам кстати", callback_data = "conch"),]
    ])


inline_keyboard_sign_in_users = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Через телеграм", callback_data = "sign_in_tg")],
    [InlineKeyboardButton(text = "По логину/паролю", callback_data = "sign_in_stand")],
    [InlineKeyboardButton(text = "Через стороннее приложение", callback_data = "sign_in_API"),]
    ])

register_button = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "регистрация"), KeyboardButton(text = "главная")]
    ], resize_keyboard = True)