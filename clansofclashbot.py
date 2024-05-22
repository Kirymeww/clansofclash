import telebot

# Создаем экземпляр бота с помощью токена
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, "На данный момент не может вести диалоги, эта функция ещё в разработке.")

# Запускаем бота
bot.polling()