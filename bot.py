from config import TOKEN
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Жопа')
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
