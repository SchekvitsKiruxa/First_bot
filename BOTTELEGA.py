import telebot
from telebot import types
Bz = telebot.TeleBot('7866982285:AAFOIeFAh7_muLORT3VEL3pOtqB_LsUBIKE')
a = 0
def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton(".")
    button2 = types.KeyboardButton(".")
    button3 = types.KeyboardButton(".")
    button4 = types.KeyboardButton(".")
    button5 = types.KeyboardButton(".")
    button6 = types.KeyboardButton(".")
    button7 = types.KeyboardButton(".")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)
    return keyboard

def create_keyboard2():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton(".")
    button2 = types.KeyboardButton(".")
    button3 = types.KeyboardButton(".")
    button4 = types.KeyboardButton(".")
    button5 = types.KeyboardButton(".")
    button6 = types.KeyboardButton(".")
    button7 = types.KeyboardButton(".")
    button8 = types.KeyboardButton(".")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8)
    return keyboard































@Bz.message_handler(commands = ["start"])
def start(m, res = False):
    Bz.send_message(m.chat.id, '.', reply_markup = create_keyboard())

@Bz.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == ".":
 	    Bz.reply_to(message, ".", reply_markup = create_keyboard2())
 	    a = 1
        
Bz.polling(none_stop=True, interval=0)
