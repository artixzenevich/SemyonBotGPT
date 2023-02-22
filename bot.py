import os
import telebot
import openai
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(telegram_bot_token)
openai.api_key = openai_api_key


@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)


bot.polling()
