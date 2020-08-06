from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

button_hello = KeyboardButton('Привет')
button_help = KeyboardButton('Помощь')
button_test = KeyboardButton('ТЕСТ')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hello)
greet_kb.add(button_help)
greet_kb.add(button_test)
