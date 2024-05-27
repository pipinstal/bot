from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я твой первый ЭХО бот')

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе с .....')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if__name__ == '__main__':
   executor.start_polling(dp, skip_updates= True)


