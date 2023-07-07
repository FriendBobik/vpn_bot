import telebot
from functions import get_text_messages

with open('token.txt', 'r') as file:
    token = file.read().strip()


bot = telebot.TeleBot(token);
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    get_text_messages(message, bot)

bot.polling(none_stop=True, interval=0)
