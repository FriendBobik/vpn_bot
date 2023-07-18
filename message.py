import telebot
import os

from telebot import types
from config import token
from work_mySQL import sql_check, sql_create,sql_free_value,sql_free_date,sql_change_free_value
from work_mySQL import sql_change_free_date,sql2_cheack,sql_date,sql_return_prof
from datetime import datetime
from consol_work import get_profil
    

    


bot = telebot.TeleBot(token)

# создаем различные клавиатуры
start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.add('Free', 'VPN', 'Информация', 'Инструкция')

free_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
free_markup.add('Да', 'В главное меню')

free_yes_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
free_yes_markup.add('Ещё', 'Бесплатный VPN действует до','В главное меню')

info_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_markup.add('О проэкте', 'Правила', 'В главное меню')

back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_markup.add('В главное меню')

devices_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
devices_markup.add('Android','Iphone', 'Windows', 'MacOS', 'Linux', 'В главное меню')

vpn_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
vpn_markup.add('Оплата', 'VPN действует до','Промокод','В главное меню')
##########################################


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=start_markup)
    #регистрация пользователя
    name = str(message.from_user.id)#получаем id пользователя
    if sql_check(int(name))==-1:    #проверяем есть ли он в базе, если пользователя не существует, функция вернет -1
        sql_create(name)            #записываем пользователя в базу
    

@bot.message_handler(content_types=['text'])
def menu_navigation(message):
    
    text1       = 'Скачай WireGuard из'
    text2       = 'Названия кликабельные'
    text21      = 'Название кликабельное'
    text3       = 'Или с официального сайта'
    text4       = 'Далее сгенерируйте профиль с помошью кнопок "Free" или "VPN"'
    text5       = 'Скачайте профиль и откройте его в WireGuard'
    text6       = 'Выбери "Импорт из файла или архива"'
    text7       = 'В предложенном меню открой папку Загрузки / Telegram, и выбери сохраненный файл.'
    text8       = 'После импорта профиля, нажмите на него и включите VPN.\nВсе работает!!!'
    text9       = 'Если у вас возникли проблемы, напишите нам в телеграмме\n(тут будет ссылка)'
    text10      = 'Скачай WireGuard с'
    text_free   = 'Ты можешь получить бесплатный профиль на 7 дней, чтобы проверить наш сервис.\nХочешь получить бесплатный профиль?'
    

    url_android = 'https://play.google.com/store/apps/details?id=com.wireguard.android'
    url_iphone  = 'https://apps.apple.com/us/app/wireguard/id1441195209'
    url_macos   = 'https://apps.apple.com/us/app/wireguard/id1451685025'
    url_site    = 'https://www.wireguard.com/install/'

    def text_itog():
        bot.send_message(message.chat.id, text4, reply_markup=back_markup)
        bot.send_message(message.chat.id, text5, reply_markup=back_markup)
        bot.send_message(message.chat.id, text6, reply_markup=back_markup)
        bot.send_message(message.chat.id, text7, reply_markup=back_markup)
        bot.send_message(message.chat.id, text8, reply_markup=back_markup)
        bot.send_message(message.chat.id, text9, reply_markup=back_markup)


    if message.text == 'В главное меню':
        bot.send_message(message.chat.id, "Возврат в главное меню", reply_markup=start_markup)
    
    #Стартовое меню
    elif message.text == 'Free':
        bot.send_message(message.chat.id, text_free, reply_markup=free_markup)
    elif message.text == 'VPN':
        bot.send_message(message.chat.id, "Test VPN", reply_markup=vpn_markup)
    elif message.text == 'Информация':
        bot.send_message(message.chat.id, "Выберите один из пунктов", reply_markup=info_markup)
    elif message.text == 'Инструкция':
        bot.send_message(message.chat.id, "Test инструкция", reply_markup=devices_markup)
    ##########################################



    #Кнопка free
    #elif message.text == 'Да':
    #    bot.send_message(message.chat.id, "Вы выбрали 'да'", reply_markup=free_yes_markup)
    ##########################################
    

    #Кнопка VPN
    elif message.text == 'Оплата':
        bot.send_message(message.chat.id, "Test оплата", reply_markup=back_markup)
    elif message.text == 'VPN действует до':
        bot.send_message(message.chat.id, "Test VPN действует до", reply_markup=back_markup)
    elif message.text == 'Промокод':
        bot.send_message(message.chat.id, "Ведите промокод:", reply_markup=back_markup)
    ##########################################


    #Кнопка информация
    elif message.text == 'О проэкте':
        bot.send_message(message.chat.id, "Test о проэкте", reply_markup=back_markup)
    elif message.text == 'Правила':
        bot.send_message(message.chat.id, "Test правила", reply_markup=back_markup)
    ##########################################




    #Кнопка инструкция
    elif message.text == 'Android':
        message_text = f'{text1} [Play market]({url_android})\n{text3} [WireGuard]({url_site})\n{text2}'
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
        text_itog()
    elif message.text == 'Iphone':
        message_text = f'{text1} [App Store]({url_iphone})\n{text21}'
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
        text_itog()
    elif message.text == 'Windows':
        message_text = f'{text10} [официального сайта]({url_site})\n{text21}'
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
        text_itog()
    elif message.text == 'MacOS':
        message_text = f'{text1} [App Store]({url_macos})\n{text3} [WireGuard]({url_site})\n{text2}'
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
        text_itog()
    elif message.text == 'Linux':
        message_text = f'{text10} [официального сайта]({url_site})\n{text21}'
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
        text_itog()
    ##########################################
    elif message.text == 'Да':
        name = str(message.from_user.id)
        if int(sql_free_value(name))==0 :
            if id==-1:   #Провереям не больше ли 5 файлов у пользователя
                bot.send_message(message.from_user.id, "Ты уже получил 5 профилей, больше нельзя")
            else:
                bot.send_message(message.from_user.id, "Почти готово, подожди 5 секунд")
                sql_change_free_value(name) #заменяем проверочное значение на 1
                sql_change_free_date(name)  #добавляем 7 дней бесплатного пользования
                id=str(sql2_cheack(name))
                get_profil(id)        #получаем профиль
                bot.send_message(message.from_user.id, "Готово:",reply_markup=free_yes_markup)
                document = open('prof/'+id+'.conf', 'rb')
                bot.send_document(message.chat.id, document)


        elif int(sql_free_value(name))==1 and sql_free_date(name) > datetime.now():
            
            id=str(sql2_cheack(name))
            if int(id)==-1:   #Провереям не больше ли 5 файлов у пользователя
                bot.send_message(message.from_user.id, "Ты уже получил 5 профилей, больше нельзя",reply_markup=back_markup)
            else:
                bot.send_message(message.from_user.id, "Почти готово, подожди 5 секунд")
                get_profil(id)        #получаем профиль
                bot.send_message(message.from_user.id, "Готово:",reply_markup=free_yes_markup)
                document = open('prof/'+id+'.conf', 'rb')
                bot.send_document(message.chat.id, document)

        elif sql_free_date(name) < datetime.now(): #бесплатное время закончилось
            bot.send_message(message.from_user.id, "Ты уже использовал бесплатный профиль, можешь воспользоваться обычным, по команде /vpn")


    elif message.text == 'Ещё':
        name = str(message.from_user.id)
        if int(sql_free_value(name))==1 and sql_free_date(name) > datetime.now():
            id=str(sql2_cheack(name))
            if int(id)==-1:   #Провереям не больше ли 5 файлов у пользователя
                bot.send_message(message.from_user.id, "Ты уже получил 5 профилей, больше нельзя",reply_markup=back_markup)
            else:
                bot.send_message(message.from_user.id, "Почти готово, подожди 5 секунд")
                get_profil(id)        #получаем профиль
                bot.send_message(message.from_user.id, "Готово:",reply_markup=free_yes_markup)
                document = open('prof/'+id+'.conf', 'rb')
                bot.send_document(message.chat.id, document)

        elif sql_free_date(name) < datetime.now(): #бесплатное время закончилось
            bot.send_message(message.from_user.id, "Ты уже использовал бесплатный профиль, можешь воспользоваться обычным, по команде /vpn")


    elif message.text == 'Бесплатный VPN действует до':
        name = str(message.from_user.id)
        data=sql_free_date(name)
        if data > datetime.now():
            bot.send_message(message.from_user.id, data,reply_markup=free_yes_markup)
        else:
            bot.send_message(message.from_user.id, "Бесплатный VPN закончился, вопсользуйся кнопкой VPN",reply_markup=back_markup)
    
    
    elif message.text == 'VPN действует до':
        name = str(message.from_user.id)
        data=sql_date(name)
        if data > datetime.now():
            bot.send_message(message.from_user.id, data,reply_markup=free_yes_markup)
        else:
            bot.send_message(message.from_user.id, "Ты не оплатил подписку",reply_markup=back_markup)

    elif message.text == 'Мои профили':
        name = str(message.from_user.id)
        values = sql_return_prof(name)
        if values:
            bot.send_message(message.from_user.id, "Твои профили:",reply_markup=back_markup)
            for value in values:
                document = open('prof/'+str(value)+'.conf', 'rb')
                bot.send_document(message.chat.id, document)
        else:
            bot.send_message(message.from_user.id, "У тебя нет профилей",reply_markup=back_markup)


    




    #Случайные сообщения
    else:
        bot.send_message(message.chat.id, "Я не понимаю эту команду",reply_markup=start_markup)
    ##########################################

bot.polling(none_stop=True, interval=0)





