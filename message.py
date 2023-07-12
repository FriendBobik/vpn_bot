def get_text_messages(message, bot):
    from consol_work import get_profil
    from work_mySQL import sql_check, sql_create

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, напиши /vpn")
        
    elif message.text == "/vpn":
        bot.send_message(message.from_user.id, "Почти готово, подожди 15 секунд")


        name = str(message.from_user.id)#получаем id пользователя
        if sql_check(int(name))==-1:    #проверяем есть ли он в базе, если пользователя не существует, функция вернет -1
            sql_create(name)            #тогда создаем запись об этом пользователе
        
        get_profil(name)

        document = open('/Users/aboba/Desktop/vpn_bot2/ecom/'+name+'.conf', 'rb')
        bot.send_message(message.from_user.id, "Готово:")
        bot.send_document(message.chat.id, document)
    
    else:
        bot.send_message(message.from_user.id, "Напиши /start.")
        