import telebot
from message import get_text_messages
from config import token
vpn_give=False



bot = telebot.TeleBot(token);
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    get_text_messages(message, bot)




bot.polling(none_stop=True, interval=0)