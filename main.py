from aiogram import  Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6666490264:AAHzGjfDtEcIR42tcjDw6R4hxdieUbuqKR8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app= WebAppInfo(url='https://github.com/21Sirius/webappsTG.git')))
    await message.answer('Привет', reply_markup= markup)

executor.start_polling(dp)