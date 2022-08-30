import os
import logging

from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#admin_id = 123456789

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_id
    #text = "Hello, {}!\n".format(message)
    text = f"Hello, {user_name}!"
    logging.info(f"{user_name=} send message: {message.text}")
    print(text)
    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_id    
    translited_text = translit(message.text)
    logging.info(f"{user_name=} send message: {translited_text}")
    await bot.send_message(user_id, translited_text)
    #await bot.send_message(admin_id, text)

def translit(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I|K|L|M|N|O|P|R|S|T|U|F|Kh|Tc|Ch|Sh|Shch||Y||E|Iu|Ia'.split('|')    
    return text.translate({ord(k):v for k,v in zip(cyrillic,latin)})     

if __name__ == '__main__':
    executor.start_polling(dp)
