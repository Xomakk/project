from telebot import types
from telebot import TeleBot

TOKEN = "7870683912:AAGajg1r_d99eemWRTodznFAaEG5gaq-2dQ"
bot = TeleBot(TOKEN)


replay_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton("Крабсбургер")
btn_2 = types.KeyboardButton("Бургер с лососем")
btn_3 = types.KeyboardButton("Бургер с бифштексом")
replay_kb.add(btn_1, btn_2, btn_3)


@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    bot.send_message(
        msg.chat.id, "Здравствуйте! Что хотите заказать?", reply_markup=replay_kb
    )


@bot.message_handler(content_types=["text"])
def handle_start(msg: types.Message):
    if msg.text == "Крабсбургер":
        pass
    elif msg.text == "Бургер с лососем":
        pass
    elif msg.text == "Бургер с бифштексом":
        pass


bot.polling(non_stop=True, interval=1)
