import telebot;

with open('token.txt', 'r') as file:
    token = file.read().strip()



bot = telebot.TeleBot(token);