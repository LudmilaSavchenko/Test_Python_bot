import telebot
import random

token = '5395629028:AAEY9svrCRXqzYcSk2-yvSVUeaA7jnWsrRg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id, "Привет ✌️ ")

"""
@bot.message_handler(commands=['button'])
def button_message(message):

  keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)
  url_button1 = telebot.types.InlineKeyboardButton("1", callback_data='1')
  url_button2 = telebot.types.InlineKeyboardButton("2", callback_data='2')
  url_button3 = telebot.types.InlineKeyboardButton("3", callback_data='3')
  keyboard.add(url_button1, url_button2, url_button3)
  bot.send_message(message.chat.id, "Сделай выбор:", reply_markup=keyboard)


  markup = telebot.types.ReplyKeyboardMarkup(row_width=2) # resize_keyboard=True
  item1 = telebot.types.KeyboardButton("МЯУ")
  item2 = telebot.types.KeyboardButton("ГАФ")
  item3 = telebot.types.KeyboardButton("МУУ")
  item4 = telebot.types.KeyboardButton("КАР")
  item5 = telebot.types.KeyboardButton("КУКАРЕКУ")
  item6 = telebot.types.KeyboardButton("ФЫР-ФЫР-ФЫР")
  markup.add(item1, item2, item3, item4, item5, item6)
  bot.send_message(message.chat.id, "Сделай выбор:", reply_markup=markup)
  """

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
  if call.data == '1':
    bot.send_message(call.message.chat.id, "Какой молодец, выбрал 1.")
  elif call.data == '2':
    bot.send_message(call.message.chat.id, "2 по 2 - это сколько лапок у котика. Вот так вот.")
  else:
    bot.send_message(call.message.chat.id, "Ну 3 можно было и не выбирать, конечно.")

@bot.message_handler(commands=['mem'])
def all_messages(message):
    #bot.send_message(message.chat.id,  "проверка. id:" + str(message.message_id))
    #my_chat_id = int(message.chat.id)
    #bot.send_message(message.chat.id, my_chat_id)
    bot.forward_message(int(message.chat.id), -1001790436083, random.randint(1,message.message_id))

bot.infinity_polling()

