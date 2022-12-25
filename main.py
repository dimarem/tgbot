if __name__ == '__main__':
    import telebot
    from config import TOKEN, commands
    from messages import start_command_message, values_command_message

    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler(commands=commands)
    def command_handler(message: telebot.types.Message):
        """Обрабатывает вводимые пользователем команды."""
        if message.text == '/start' or message.text == '/help':
            bot.reply_to(message, start_command_message)
        elif message.text == '/values':
            bot.reply_to(message, values_command_message)


    bot.polling(none_stop=True)
