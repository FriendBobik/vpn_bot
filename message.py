def get_text_messages(message, bot):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, напиши /vpn")
    elif message.text == "/vpn":
        bot.send_message(message.from_user.id, "Нужен VPN круто")
        vpn_start=1
    else:
        bot.send_message(message.from_user.id, "Напиши /start.")