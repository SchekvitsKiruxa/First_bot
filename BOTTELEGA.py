import telebot
from telebot import types
Bz = telebot.TeleBot('')
def create_keyboard():#Типы блюд
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("Закуска")
    button2 = types.KeyboardButton("Первое")
    button3 = types.KeyboardButton("Горячее")
    button4 = types.KeyboardButton("Десерт")
    button5 = types.KeyboardButton("Напитки")
    keyboard.add(button1, button2, button3, button4, button5)
    return keyboard

def create_keyboard2():#Закуски
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("Тарталетка с курицей и грибами в духовке")
    button2 = types.KeyboardButton("Холодец")
    button3 = types.KeyboardButton("Салат Винегрет")
    button4 = types.KeyboardButton("Жульен")
    keyboard.add(button1, button2, button3, button4)
    return keyboard

def create_keyboard3():#Первое
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("Борщ")
    button2 = types.KeyboardButton("Щи")
    button3 = types.KeyboardButton("Солянка")
    keyboard.add(button1, button2, button3)
    return keyboard

def create_keyboard4():#Горячее
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("Жаркое")
    button2 = types.KeyboardButton("Лазанья")
    button3 = types.KeyboardButton("Плов")
    keyboard.add(button1, button2, button3)
    return keyboard

def create_keyboard5():#Десерт
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("Торт")
    button2 = types.KeyboardButton("Мороженное")
    button3 = types.KeyboardButton("Пирог")
    keyboard.add(button1, button2, button3)
    return keyboard


def create_keyboard6():#Напитки
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("Морс")
    button2 = types.KeyboardButton("Квас")
    button3 = types.KeyboardButton("Сбитень")
    keyboard.add(button1, button2, button3)
    return keyboard










@Bz.message_handler(commands = ["start"])
def start(m, res = False):
    Bz.send_message(m.chat.id, 'Здравствуйте это поваренная книга в виде бота.Какой вам нужен рецепт?', reply_markup = create_keyboard())

@Bz.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "Закуска":
 	    Bz.reply_to(message, ".", reply_markup = create_keyboard2())
    if message.text == "Первое":
 	    Bz.reply_to(message, ".", reply_markup = create_keyboard3())
    if message.text == "Горячее":
 	    Bz.reply_to(message, ".", reply_markup = create_keyboard4())
    if message.text == "Десерт":
 	    Bz.reply_to(message, ".", reply_markup = create_keyboard5())
    if message.text == "Напитки":
 	    Bz.reply_to(message, ".", reply_markup = create_keyboard6())




 	    
        
Bz.polling(none_stop=True, interval=0)

