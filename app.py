import telebot
from telebot import types

# Замените 'YOUR_BOT_API_TOKEN' на токен вашего бота
API_TOKEN = '5643214146:AAFq5PUla29scsQm8evsNwV4dbeD4TDpXUU'
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш бот для открытия MiniApps. Используйте команду /open_miniapp.")

# Команда /open_miniapp
@bot.message_handler(commands=['open_miniapp'])
def open_miniapp(message):
    # Здесь можно добавить логику для открытия MiniApps
    # Например, отправка URL-адреса MiniApp пользователю
    miniapp_url = "https://t.me/coddytest99bot/CoddysSnake"  # Замените на URL вашего MiniApp
    bot.reply_to(message, f"Открыть MiniApp: {miniapp_url}")

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Пожалуйста, используйте команды /start или /open_miniapp.")

# Запуск бота
bot.polling()
