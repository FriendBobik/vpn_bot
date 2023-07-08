def get_text_messages(message, bot):
    import re
    from consol_work import get_profil
    from datetime import datetime

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, напиши /vpn")
        
    elif message.text == "/vpn":
        bot.send_message(message.from_user.id, "Нужен VPN? Подожди 10 секунд")
        name = message.from_user.first_name

        

        def contains_cyrillic(name):
            return bool(re.search('[а-яА-Я]', name))
        if contains_cyrillic(name)==True:
            now=datetime.now()
            name=now
        if len(name) > 15:
             name = name[:15]
        get_profil(name)
        print('cool')


        document = open('/Users/aboba/Desktop/vpn_bot2/ecom/wg0-client-'+name+'.conf', 'rb')
        bot.send_message(message.from_user.id, "Готово:")
        bot.send_document(message.chat.id, document)

    else:
        bot.send_message(message.from_user.id, "Напиши /start.")
        