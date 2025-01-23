import os
from dotenv import load_dotenv
import telebot
from telebot.types import Message

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
KEYWORDS = ['Jasur', 'jasur']

bot = telebot.TeleBot(BOT_TOKEN)

@bot.channel_post_handler(func=lambda message: any(keyword in message.text.lower() for keyword in KEYWORDS))
def edit_message(message: Message):
    try:
        text = message.text
        for keyword in KEYWORDS:
            text = text.replace(keyword, '')
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f"<creator>{text.strip()}</creator>")
        print("Bot is running and editing messages.")
    except Exception as e:
        print(f"Error: {e}")

bot.polling(none_stop=True)