import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv('TOKEN'))


def main():
    print(bot.token)


if __name__ == '__main__':
    main()
