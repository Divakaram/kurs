import telebot
from djagriti.settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
chat_id = "-604669800"


def send_message(tg_name, tg_phone):
    bot.send_message(chat_id, f"Заявка с сайта:\nИмя: {tg_name}\n"
                              f"Телефон:{tg_phone}")

bot.polling()
