import telebot
import os
from dotenv import load_dotenv, find_dotenv

import commands
from commands import checkCommand

load_dotenv(find_dotenv())


bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    bot_msg = ''
    if checkCommand(message.text, commands.START):
        bot_msg = f'Привет, <b>{message.from_user.first_name}</b>!\n' \
                  f'Введи команду /help для просмотра справки.'
    elif checkCommand(message.text, commands.HELP):
        bot_msg = 'Данный раздел находится в стадии разработки.'

    bot.send_message(message.chat.id, bot_msg, parse_mode='html')


@bot.message_handler()
def other_handler(message):
    bot_msg = 'Пока что я не научился отвечать на такие запросы.\n' \
              'Введите /help для просмотра списка доступных комманд.'

    bot.send_message(message.chat.id, bot_msg, parse_mode='html')


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
