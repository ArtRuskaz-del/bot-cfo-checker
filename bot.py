import telebot
from telebot.types import Update
from flask import Flask, request

API_TOKEN = '8025301276:AAETwHjHF7MJzmNCm_mKSDM_vWtQmmb8ZdY'
CHANNEL_USERNAME = '@CFO_na_svyazi'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# === Команда /start ===
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ['member', 'administrator', 'creator']:
            bot.send_message(
                message.chat.id,
                "Вы подписаны! Вот ваша ссылка для скачивания:\nhttps://docs.google.com/document/d/1CEBStQvs52MK434ifdJQmDR6NHReyo6Uca08I5Y2hmM/edit?usp=sharing"

            )
        else:
            bot.send_message(
                message.chat.id,
                "Чтобы получить доступ, подпишитесь на канал:\nhttps://t.me/CFO_na_svyazi"
            )

    except:
        bot.send_message(
            message.chat.id,
            "Чтобы получить доступ, подпишитесь на канал:\nhttps://t.me/CFO_na_svyazi"
        )

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.data:
        update = Update.de_json(request.get_json(force=True))
        bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
