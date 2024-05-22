import telebot

# Создаем экземпляр бота с помощью токена
bot = telebot.TeleBot('7179938903:AAHIli8J27QvKM5V0CS2FmK2L-I1ZW3aSHc')

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, "На данный момент не может вести диалоги, эта функция ещё в разработке.")

# Запускаем бота
bot.polling()
