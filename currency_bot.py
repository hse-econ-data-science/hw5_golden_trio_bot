#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
import telebot
from pycbrf import ExchangeRates

bot = telebot.TeleBot('1767654345:AAGNh_FjXoXeFdVD9eE5wDnRHHJTQyhRrAo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Приветики!🖐 Хотите увидеть курсы обмена валют?\n' +
        'Чтобы узнать курсы обмена, напишите мне "/обмен".\n' +
        'Чтобы получить помощь напишите мне "/помощь".'
  )

@bot.message_handler(commands=['помощь'])
def help_(message):
    bot.send_message(
        message.chat.id,
        '1️⃣ Чтобы получить список доступных валют, напишите "/обмен".\n' +
        '2️⃣ Выберете нужную валюту.\n' +
        '3️⃣ Вы получите сообщение, содержащее информацию об обменном курсе.\n'
    )

@bot.message_handler(commands=['обмен'])
def exchange(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    itembtn3 = telebot.types.KeyboardButton('GBP')
    itembtn4 = telebot.types.KeyboardButton('UAH')
    itembtn5 = telebot.types.KeyboardButton('CNY')
    keyboard.add(itembtn1, itembtn2, itembtn3,  itembtn4, itembtn5)
    bot.send_message(chat_id=message.chat.id, text="Выберете интересующую валюту из предложенных:", reply_markup=keyboard, parse_mode="html")
@bot.message_handler(content_types=['text'])
def message(message):
    query = message.text.strip().lower()
    
    if query in ["usd", "eur", "gbp", "uah", "cny"]:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text=f"<b><i> 💰 Курс {query.upper()} - {float(rates[query.upper()].rate)} RUB</i></b>", parse_mode="html")
bot.polling(none_stop=True)


# In[ ]:





# In[ ]:




