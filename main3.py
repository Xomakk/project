from telebot import types
from telebot import TeleBot
import random
import string

TOKEN = "7870683912:AAE5aDJp6MfQ1a40qBOLVEVlAxjqI20aPgw"
bot = TeleBot(TOKEN)

def generate_password(n):
    res = " "
    symbols = string.ascii_letters + string.digits + string.punctuation
    for i in range(n):
        res += random.choice(symbols)
    return res

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add("Сгенерировать пароль")

@bot.message_handler(commands=['start'])
def handle_start(msg: types.Message):
    bot.send_message(
        msg.chat.id, 
        "Привет! Я умею генерить надежные пароли ^_^",
        reply_markup=kb
    )
    
@bot.message_handler(content_types=["text"])
def handle_message(msg: types.Message):
    if msg.text == "Сгенерировать пароль":
        pswrd = generate_password(10)
        bot.send_message(msg.chat.id, f"Ваш пароль: {pswrd}")

print("Сервер запущен.")
bot.polling(non_stop=True, interval=1)
