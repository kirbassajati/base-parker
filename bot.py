import telebot

# =====================================
# CONFIG
# =====================================

TOKEN = "TOKEN_BOT_KAMU"

# ID CHANNEL
CHANNEL_ID = -1003949063805

# ID GROUP DISKUSI / KOMENTAR
DISCUSSION_GROUP_ID = -1003917990426

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
# FILTER KATA
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

    teks = """
parker di sini, ada parker jangan lari 🐾

send menfess kamu ya!
taati peraturan di @parkerinfo
"""

    bot.reply_to(message, teks)

# =====================================
# TEXT
# =====================================

@bot.message_handler(
    content_types=['text'],
    func=lambda m: m.chat.type == "private"
)
def handle_text(message):

    try:

        # filter kata terlarang
        if contains_bad_words(message.text):

            bot.reply_to(
                message,
                "❌ Pesan mengandung kata terlarang."
            )

            return

        # kirim ke channel
        sent = bot.send_message(
            CHANNEL_ID,
            message.text
        )

        # link post
        post_link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.message_id}"

        # kirim komentar otomatis ke grup diskusi
        komentar = """
Ada scammer/rusuh? Tag @admin
atau /report 3x maka otomatis kebanned

Open paid promote
Check @parkerinfo
"""

        bot.send_message(
            DISCUSSION_GROUP_ID,
            komentar
        )

        # notif user
        bot.reply_to(
            message,
            f"✅ Pesan terkirim!\n\n🔗 Link menfess:\n{post_link}"
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

        # filter kata
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

        # link post
        post_link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.message_id}"

        # komentar otomatis
        komentar = """
Ada scammer/rusuh? Tag @admin
atau /report 3x maka otomatis kebanned

Open paid promote
Check @parkerinfo
"""

        bot.send_message(
            DISCUSSION_GROUP_ID,
            komentar
        )

        # notif user
        bot.reply_to(
            message,
            f"✅ Foto berhasil terkirim!\n\n🔗 Link menfess:\n{post_link}"
        )

    except Exception as e:
        print("ERROR FOTO:", e)

# =====================================
# RUN
# =====================================

print("BOT ONLINE")

bot.infinity_polling(
    skip_pending=True,
    none_stop=True
)
