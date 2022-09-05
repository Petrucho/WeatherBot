import os
import logging
import getipinfo
import getweather
import public_ip as ip
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    text = f"Hello, {user_name}!\nYour coordinates is: {getipinfo.get_info(ip.get())}\nThe weather in this location: {getweather.get_weather()}"
    logging.info(f"{user_name=} send message: {message.text}")
    print(text)
    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_id
    text = f"The weather in your location: {getweather.get_weather()}"
    logging.info(f"{user_name=} send message: {message.text}")    
    await bot.send_message(user_id, text)
    #await bot.send_message(admin_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)
