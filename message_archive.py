def get_text_messages(message, bot):
    from consol_work import get_profil
    from work_mySQL import sql_check, sql_create,sql_free_value,sql_free_date,sql_change_free_value
    from work_mySQL import sql_change_free_date
    from datetime import datetime
    

    import os



    if message.text == "/start":
        
        #регистрация пользователя
        name = str(message.from_user.id)#получаем id пользователя
        if sql_check(int(name))==-1:    #проверяем есть ли он в базе, если пользователя не существует, функция вернет -1
            sql_create(name)            #записываем пользователя в базу
        
        
        #тут надо добвать кнопочки,free, vpn,info,instr

    elif message.text == "/free_vpn":
        name = str(message.from_user.id)
        if int(sql_free_value(name))==0:
            bot.send_message(message.from_user.id, "Почти готово, подожди 15 секунд")
            sql_change_free_value(name) #заменяем проверочное значение на 1
            sql_change_free_date(name)  #добавляем 7 дней бесплатного пользования
            get_profil(name)            #получаем профиль
            bot.send_message(message.from_user.id, "Готово:")
            document = open(name+'.conf', 'rb')
            bot.send_document(message.chat.id, document)
        elif sql_free_date(name) > datetime.now(): #бесплатное время ещё не закончилось
            if os.path.exists(name+'.conf'):       #дублируем файл
                document = open(name+'.conf', 'rb')
                bot.send_message(message.from_user.id, "Ты уже генерировал профиль, вот он:")
                bot.send_document(message.chat.id, document)
            else:
                bot.send_message(message.from_user.id, "Куда спешишь подожди") #защита от перегрузки
        elif sql_free_date(name) < datetime.now(): #бесплатное время ещё закончилось
            bot.send_message(message.from_user.id, "Ты уже использовал бесплатный профиль, можешь воспользоваться обычным, по команде /vpn")

    elif message.txt == "/vpn":
        return 0
    elif message.txt == "/info":
        return 0

        

        

    

        
    
    else:
        bot.send_message(message.from_user.id, "Напиши /start.")
        