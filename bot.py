import imp
import os
import logging
from urllib import request

from aiogram import Bot, Dispatcher, executor, types
from aiogram import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

logging.basicConfig(level=logging.INFO)

# TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#admin_id = 123456789

button1 = KeyboardButton('Send location', request_location=True)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name    
    #text = "Hello, {}!\n".format(message)
    text = f"Hello, {user_name}!"
    logging.info(f"{user_name=} send message: {message.text}")
    print(text)
    await message.reply(text, reply_markup=keyboard1)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_id    
    user_long = message.location.longitude
    # message.location.longitude
    # user_lat = message.location.latitude
    print(f'user_long: {user_long}')
    # print(f'user_lat: {user_lat}')
    translited_text = translit(message.text)
    # logging.info(f"{user_name=} send message: {translited_text}")
    logging.info(f"{user_name=} send message: {user_long}")
    # await bot.send_message(user_id, translited_text)
    await bot.send_message(user_id, user_long)
    #await bot.send_message(admin_id, text)

# @dp.message_handler(content_types=['location'])
# def handle_location(message):
#     print("{0}, {1}".format(message.location.latitude, message.location.longitude))

if __name__ == '__main__':
    executor.start_polling(dp)
