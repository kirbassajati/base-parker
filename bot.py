import telebot

TOKEN = "8662189428:AAHE702xAkCJ9Mie-_4XsLrsKyomFcSLSTQ"

CHANNEL_ID = -1003949063805

bot = telebot.TeleBot(TOKEN)

# =========================
# KATA TERLARANG
# =========================

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

# =========================
# FILTER KATA
# =========================

def contains_bad_words(text):

    text = text.lower()

    for word in BAD_WORDS:

        if word.lower() in text:
            return True

    return False

# =========================
# START
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(
        message,
        "👋 Kirim menfess text atau foto."
    )

# =========================
# TEXT
# =========================

@bot.message_handler(
    content_types=['text'],
    func=lambda m: m.chat.type == "private"
)
def handle_text(message):

    try:

        if contains_bad_words(message.text):

            bot.reply_to(
                message,
                "❌ Pesan mengandung kata terlarang."
            )
            return

        teks = f"""
{message.text}

━━━━━━━━━━━━━━
scam, perusuh, penipu tag @admins
informasi base & paid promote @parkerinfo
"""

        bot.send_message(
            CHANNEL_ID,
            teks
        )

    except Exception as e:
        print(e)

# =========================
# FOTO
# =========================

@bot.message_handler(
    content_types=['photo'],
    func=lambda m: m.chat.type == "private"
)
def handle_photo(message):

    try:

        caption = ""

        if message.caption:
            caption = message.caption

        if contains_bad_words(caption):

            bot.reply_to(
                message,
                "❌ Caption mengandung kata terlarang."
            )
            return

        caption_final = f"""
{caption}

━━━━━━━━━━━━━━
scam, perusuh, penipu tag @admins
informasi base & paid promote @parkerinfo
"""

        bot.send_photo(
            CHANNEL_ID,
            message.photo[-1].file_id,
            caption=caption_final
        )

    except Exception as e:
        print(e)

# =========================
# RUN
# =========================

print("BOT ONLINE")

bot.infinity_polling(skip_pending=True)
