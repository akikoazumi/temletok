from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#some code

studyboi = InlineKeyboardButton('Channel Bot', url='https://t.me/nekozu')
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(studyboi)
