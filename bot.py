import telebot

# =====================================
# CONFIG
# =====================================

TOKEN = "8662189428:AAHE702xAkCJ9Mie-_4XsLrsKyomFcSLSTQ"
CHANNEL_ID = -1003949063805

bot = telebot.TeleBot(TOKEN)

# =====================================
# KATA TERLARANG
# =====================================

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
    "maker"
]

# =====================================
# CEK KATA TERLARANG
# =====================================

def contains_bad_words(text):

    text = text.lower()

    for word in BAD_WORDS:

        if word.lower() in text:
            return True

    return False

# =====================================
# START
# =====================================

@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(
        message,
        "👋 Kirim menfess text atau foto."
    )

# =====================================
# TEXT
# =====================================

@bot.message_handler(
    content_types=['text'],
    func=lambda m: m.chat.type == "private"
)
def handle_text(message):

    try:

        # cek kata terlarang
        if contains_bad_words(message.text):

            bot.reply_to(
                message,
                "❌ Pesan mengandung kata terlarang."
            )

            return

        # kirim post utama
        sent = bot.send_message(
            CHANNEL_ID,
            message.text
        )

        # komentar otomatis
        komentar = """
scam, perusuh, penipu tag @admins
informasi base & paid promote @parkerinfo
"""

        bot.send_message(
            CHANNEL_ID,
            komentar,
            reply_to_message_id=sent.message_id
        )

    except Exception as e:
        print("ERROR TEXT:", e)

# =====================================
# FOTO
# =====================================

@bot.message_handler(
    content_types=['photo'],
    func=lambda m: m.chat.type == "private"
)
def handle_photo(message):

    try:

        caption = message.caption or ""

        # cek kata terlarang
        if contains_bad_words(caption):

            bot.reply_to(
                message,
                "❌ Caption mengandung kata terlarang."
            )

            return

        # kirim foto
        sent = bot.send_photo(
            CHANNEL_ID,
            message.photo[-1].file_id,
            caption=caption
        )

        # komentar otomatis
        komentar = """
scam, perusuh, penipu tag @admins
informasi base & paid promote @parkerinfo
"""

        bot.send_message(
            CHANNEL_ID,
            komentar,
            reply_to_message_id=sent.message_id
        )

    except Exception as e:
        print("ERROR FOTO:", e)

# =====================================
# RUN BOT
# =====================================

print("BOT ONLINE")

bot.infinity_polling(
    skip_pending=True,
    none_stop=True
)
