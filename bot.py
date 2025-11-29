import telebot
import os

# TOKEN мы возьмём из переменных окружения Render
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте! 👋\n"
        "Я бот студии <b>Neonbot Studio</b>.\n"
        "Бот работает! 🚀\n\n"
        "Напишите /start чтобы начать."
    )

bot.infinity_polling(skip_pending=True)
