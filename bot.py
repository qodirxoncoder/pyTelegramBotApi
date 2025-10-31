from telebot import types
import telebot

bot = telebot.TeleBot("8369232981:AAHge7FHGbqRrs0yVD-aP8T5yTSOYMcoWJM")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Ha", callback_data="yes")
    btn2 = types.InlineKeyboardButton("Yo'q", callback_data="no")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Salom! Tugmani bosing:", reply_markup=markup)

# Callback handler
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "yes":
        bot.answer_callback_query(call.id, "Siz Ha tugmasini bosdingiz ✅")
    elif call.data == "no":
        bot.answer_callback_query(call.id, "Siz Yo'q tugmasini bosdingiz ❌")

bot.polling()
