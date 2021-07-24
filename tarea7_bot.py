import os
import telebot

bot=telebot.TeleBot('1948675820:AAFK_j8Xur0rF1Fgf_A1dmE-FIJm6hkOdZ4')

@bot.message_handler(commands=['fahrenheit'])

def fa(m):
    cid=m.chat.id
    bot.send_photo(cid,open('celcius-a-fahrenheit.jpg','rb'))

@bot.message_handler(commands=['celcius'])

def celcius(m):
    cid=m.chat.id
    bot.send_photo(cid,open('fahrenheit-a-celcius.jpg','rb'))

bot.polling()