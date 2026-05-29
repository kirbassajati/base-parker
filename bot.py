import telebot

TOKEN = "8662189428:AAHE702xAkCJ9Mie-_4XsLrsKyomFcSLSTQ"

bot = telebot.TeleBot(TOKEN)

TARGET = -1003949063805

BAD_WORDS = [
    "join ress",
    "reseller",
    "admin lain",

    "murah di",
    "join channel",
    "cek channel",
    "subs channel",

    "wa.me",
    "whatsapp",
    "t.me/",
    "telegram.me",

    "@gmail",

    "pc aja",
    "private chat",
    "chat pribadi",

    "open ress",
    "open reseller",
    "open admin",

    "promosi",
    "partner lain",
    "owner lain",
    "fristhand",

    "maker",
    "tawarin"
]

# start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🐕‍🦺 kirim pesan menfess kamu."
    )

# menfess
@bot.message_handler(func=lambda m: True)
def menfess(message):

    text = message.text

    # abaikan command
    if text.startswith("/"):
        return

    # filter kata terlarang
    for bad in BAD_WORDS:
        if bad in text.lower():

            bot.reply_to(
                message,
                "❌ pesan mengandung kata terlarang"
            )
            return

    # kirim ke channel
    bot.send_message(
        TARGET,
        f"{text}"
    )

    # balasan keuser
    bot.reply_to(
        message,
        '✅ pesan berhasil terkirim!'
    )

print("Bot aktif...")
bot.infinity_polling(skip_pending=True)