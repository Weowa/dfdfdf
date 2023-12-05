import telebot
from telebot import types


bot = telebot.TeleBot('6923395727:AAFGPkkWP2A57u6oZzCEEVIEyKNShK7ltw8')


@bot.message_handler(command=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Перейти по ссылке", url="https://t.me/+zAP5c7dsyoFjYTE6")
    markup.add(btn1)
    bot.send_message(message.from_user.id,'Ссылка на группу',reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "hello":
        markup = types.replyKeyboardMarkup(resize_keyboard = True)
        btn1= types.KeyboardButton("кнопка 1")
        btn2= types.KeyboardButton("кнопка 2")
        btn3 = types.KeyboardButton("кнопка 3")
        markup.add(btn1,btn2,btn3)
    
    elif message.text == "кнопка 1":
       bot.send_message(message.from_user.id,"нажата кнопка 1", parse_mode='Markdown') 
       
    elif message.text == "кнопка 2":
       bot.send_message(message.from_user.id,"нажата кнопка 2", parse_mode='Markdown') 

    elif message.text == "кнопка 3":
       bot.send_message(message.from_user.id,"нажата кнопка 3", parse_mode='Markdown') 
    
bot.polling(non_stop=True, interval=0)