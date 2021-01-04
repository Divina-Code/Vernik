import telebot
from random import randint as rid

bot = telebot.TeleBot('1318126041:AAG2SSb6ZYtzTsuc0LtoWkjz3Q7TIhpEn28')
@bot.message_handler(content_types=['text'])
def ans_mess(message):
    mes = message.text
    user = message.chat.username
    id = message.chat.id
    bot.send_message(id, "Enter word")
    inp = message.text.lower().split()
    for word in inp:
        if word[::-1] ==word:
            bot.send_message(id, "that word is palindrom")
        else:
            bot.send_message(id, "that word isn`t palindrom")
