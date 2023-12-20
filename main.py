import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked

API_TOKEN = 'Bot-Token'

logging.basicConfig(level=logging.DEBUG )

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text=f'Salom, {message.from_user.full_name}!'
    )
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await asyncio.sleep(20)
    await message.reply(text="Nima yordam kerak")

@dp.message_handler(commands=['dice'])
async def dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

@dp.message_handler(commands='html')
async def html(message: types.Message):
    await message.answer(
        text=f'<b>{message.from_user.first_name}</b>\n<em>{message.from_user.last_name}</em>\n<u>{message.from_user.username}</u>'
        f'\n<strike>Real madrid</strike>\n<code>{message.from_user.id}</code>\n'
        f'<a href="tg://user?id={message.from_user.id}">bir bala</a>\n'
        f'<a href="google.com">oddiy havola</a>',
        parse_mode="HTML"
    )

@dp.message_handler(commands=['markdown'])
async def markdown(message: types.Message):
    await message.answer(
        text="*qalin*\n_Kursiv_",
        parse_mode="MarkdownV2"
    )


@dp.errors_handler(exception=BotBlocked)
async def bot_blocked(update: types.Update, expection: Exception):
    print(f"Menimcha meni kimdir bloklab qo`ygan.\nXabar: {update}\nIstisno: {expection}")
    return True


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)




# @dp.message_handler(content_types=["photo", "document"])
# async def get_photo(message: types.Message):
#     await message.answer(
#         text='Siz rasm yoki hujjat jo`natdingiz'
#     )
#
# @dp.message_handler(content_types=["sticker"])
# async def get_sticker(message: types.Message):
#     await message.answer(
#         text='Siz sticker jo`natdingiz'
#     )
# @dp.message_handler(content_types=types.ContentType.AUDIO)
# async def get_audio(message: types.Message):
#     await message.answer(
#         text='Siz audio jo`natdingiz'
#     )
# @dp.message_handler(content_types=types.ContentType.VOICE)
# async def get_voice(message: types.Message):
#     await message.answer(
#         text='Siz voice jo`natdingiz'
#     )
#
# @dp.message_handler(content_types=types.ContentType.VIDEO)
# async def get_video(message: types.Message):
#     await message.answer(
#         text='Siz video jo`natdingiz'
#     )