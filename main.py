if __name__ == '__main__':
    import telebot
    from config import TOKEN, commands, content_types
    from messages import start_command_message, values_command_message
    from classes import APIException, Converter, RequestParser

    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler(commands=commands)
    def command_handler(message: telebot.types.Message):
        """Обрабатывает вводимые пользователем команды."""
        if message.text == '/start' or message.text == '/help':
            bot.reply_to(message, start_command_message)
        elif message.text == '/values':
            bot.reply_to(message, values_command_message)


    @bot.message_handler(content_types=content_types)
    def request_handler(message: telebot.types.Message):
        try:
            base, quote, amount = RequestParser.parse_request(message.text)
            result = Converter.get_price(base, quote, amount)
            bot.reply_to(message, result)
        except APIException as e:
            bot.reply_to(message, e)


    bot.polling(none_stop=True)
