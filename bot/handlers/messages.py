from aiogram.types import Message
from bot import dp, bot
from bot.api import MobileTikTokAPI, TikTokAPI


platforms = [MobileTikTokAPI(), TikTokAPI()]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hai Aku Adalah Bot Untuk Mendownload Video Tiktok Tanpa Watermark. Silahkan Kirim Videonya Kesini. Powered By @aiogram!")

@dp.message_handler()
async def get_message(message: Message):
    for api in platforms:
        if videos := [v for v in await api.handle_message(message) if v and v.content]:
            for video in videos:
                await bot.send_video(
                    message.chat.id, video.content, reply_to_message_id=message.message_id
                )
            break
