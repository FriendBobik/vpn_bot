with open('token.txt', 'r') as file:
    token = file.read().strip()



import telebot;
bot = telebot.TeleBot(token);