from telebot import types
import telebot

bot = telebot.TeleBot("8369232981:AAHge7FHGbqRrs0yVD-aP8T5yTSOYMcoWJM")


# /start komandasi
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Salom de", callback_data="greet")
    btn2 = types.InlineKeyboardButton("Rasm yubor", callback_data="send_image")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Salom! Quyidagi tugmalardan birini bosing:", reply_markup=markup)

# Callback handler
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "greet":
        bot.answer_callback_query(call.id, "Salom! 😊")
        bot.send_message(call.message.chat.id, "Siz salom tugmasini bosdingiz!")
    elif call.data == "send_image":
        bot.answer_callback_query(call.id, "Rasm yuborildi 📷")
        # Rasmni yuborish (shu fayl sizning loyihangizda bo‘lishi kerak)
        with open("example.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo)

bot.polling()

