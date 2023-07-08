import telebot
from message import get_text_messages
vpn_start=0


with open('token.txt', 'r') as file:
    token = file.read().strip()


bot = telebot.TeleBot(token);
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    get_text_messages(message, bot)


if (vpn_start==1):
    print(5)




bot.polling(none_stop=True, interval=0)