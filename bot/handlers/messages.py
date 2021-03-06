from aiogram.types import Message
from bot import dp, bot
from aiogram import types
from bot.api import MobileTikTokAPI, TikTokAPI
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.inline_keyboard import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
#some code

platforms = [MobileTikTokAPI(), TikTokAPI()]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi 👋 I'm a tik tok downloader bot! just send video link! 📱 join : @akarida")


@dp.message_handler()
async def get_message(message: Message):
    for api in platforms:
        if videos := [v for v in await api.handle_message(message) if v and v.content]:
            for video in videos:
                await bot.send_video(
                    message.chat.id, video.content, reply_to_message_id=message.message_id
                )
            break
