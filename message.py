def get_text_messages(message, bot):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")