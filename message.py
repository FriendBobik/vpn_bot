def get_text_messages(message, bot):
    from consol_work import get_profil

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, напиши /vpn")
        
    elif message.text == "/vpn":
        bot.send_message(message.from_user.id, "Почти готово, подожди 15 секунд")
        name = str(message.from_user.id)
        get_profil(name)
        document = open('/Users/aboba/Desktop/vpn_bot2/ecom/'+name+'.conf', 'rb')
        bot.send_message(message.from_user.id, "Готово:")
        bot.send_document(message.chat.id, document)
    
    else:
        bot.send_message(message.from_user.id, "Напиши /start.")
        