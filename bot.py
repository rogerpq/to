from datetime import datetime
bot = telebot.TeleBot("5558725774:AAEnwhCn5sHEobHy8Sp2xoZV5VvZUdczWJo")
@bot.message_handler(commands=['/time'])
def send_time(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    bot.reply_to(message, f"The current time is {current_time} on {current_date}")
bot.polling()
