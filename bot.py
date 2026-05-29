import telebot
import time

# =====================================
# CONFIG
# =====================================

TOKEN = "8662189428:AAHE702xAkCJ9Mie-_4XsLrsKyomFcSLSTQ"

# ID CHANNEL
CHANNEL_ID = -1003949063805

# ID GROUP DISKUSI
DISCUSSION_GROUP_ID = -1003917990426

bot = telebot.TeleBot(TOKEN)

# =====================================
# MODE BOT
# =====================================

BOT_AKTIF = True

ALASAN_MAINTENANCE = "maintenance"

# =====================================
# LIMIT MENFESS
# =====================================

MAX_CONFESS = 35

# penyimpanan limit user
user_limit = {}

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
# CEK LIMIT
# =====================================

def check_limit(user_id):

    if user_id not in user_limit:
        user_limit[user_id] = 0

    if user_limit[user_id] >= MAX_CONFESS:
        return False

    return True

# =====================================
# START
# =====================================

@bot.message_handler(commands=['start'])
def start(message):

    teks = f"""
🛺 parker menfess bot

send menfess kamu sekarang!

📦 Limit:
{MAX_CONFESS} menfess / akun

taati rules di @parkerinfo
"""

    bot.reply_to(message, teks)

# =====================================
# COMMAND LIMIT
# =====================================

@bot.message_handler(commands=['limit'])
def cek_limit(message):

    user_id = message.from_user.id

    if user_id not in user_limit:
        user_limit[user_id] = 0

    sisa = MAX_CONFESS - user_limit[user_id]

    bot.reply_to(
        message,
        f"""
📦 Sisa limit kamu:
{sisa}/35
"""
    )

# =====================================
# TEXT MENFESS
# =====================================

@bot.message_handler(
    content_types=['text'],
    func=lambda m: m.chat.type == "private"
)
def handle_text(message):

    try:

        # =====================================
        # CEK STATUS BOT
        # =====================================

        if not BOT_AKTIF:

            bot.reply_to(
                message,
                f"""
❌ Bot nonaktif sementara

Alasan:
{ALASAN_MAINTENANCE}
"""
            )

            return

        user_id = message.from_user.id

        # =====================================
        # CEK LIMIT
        # =====================================

        if not check_limit(user_id):

            bot.reply_to(
                message,
                """
❌ Limit menfess kamu habis

📦 Limit:
35/35

silakan tunggu reset limit
"""
            )

            return

        # =====================================
        # FILTER KATA
        # =====================================

        if contains_bad_words(message.text):

            bot.reply_to(
                message,
                "❌ Pesan mengandung kata terlarang."
            )

            return

        # =====================================
        # KIRIM MENFESS
        # =====================================

        sent = bot.send_message(
            CHANNEL_ID,
            f"🛺 {message.text}"
        )

        # =====================================
        # TAMBAH LIMIT
        # =====================================

        user_limit[user_id] += 1

        sisa = MAX_CONFESS - user_limit[user_id]
# =====================================
        # LINK POST
        # =====================================

        post_link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.message_id}"

        # =====================================
        # AUTO KOMENTAR
        # =====================================

        komentar = """
🛺 parker auto reply

Ada scammer/rusuh?
Tag @admin atau /report 3x

Open paid promote
Check @parkerinfo
"""

        bot.send_message(
            DISCUSSION_GROUP_ID,
            komentar
        )

        # =====================================
        # NOTIF USER
        # =====================================

        bot.reply_to(
            message,
            f"""
✅ Menfess berhasil terkirim

📦 Sisa limit:
{sisa}/35

🔗 Link menfess:
{post_link}
"""
        )

    except Exception as e:
        print("ERROR TEXT:", e)

# =====================================
# FOTO MENFESS
# =====================================

@bot.message_handler(
    content_types=['photo'],
    func=lambda m: m.chat.type == "private"
)
def handle_photo(message):

    try:

        # =====================================
        # CEK STATUS BOT
        # =====================================

        if not BOT_AKTIF:

            bot.reply_to(
                message,
                f"""
❌ Bot nonaktif sementara

Alasan:
{ALASAN_MAINTENANCE}
"""
            )

            return

        user_id = message.from_user.id

        # =====================================
        # CEK LIMIT
        # =====================================

        if not check_limit(user_id):

            bot.reply_to(
                message,
                """
❌ Limit menfess kamu habis

📦 Limit:
35/35

silakan tunggu reset limit
"""
            )

            return

        caption = message.caption or ""

        # =====================================
        # FILTER KATA
        # =====================================

        if contains_bad_words(caption):

            bot.reply_to(
                message,
                "❌ Caption mengandung kata terlarang."
            )

            return

        # =====================================
        # KIRIM FOTO
        # =====================================

        sent = bot.send_photo(
            CHANNEL_ID,
            message.photo[-1].file_id,
            caption=f"🛺 {caption}"
        )

        # =====================================
        # TAMBAH LIMIT
        # =====================================

        user_limit[user_id] += 1

        sisa = MAX_CONFESS - user_limit[user_id]

        # =====================================
        # LINK POST
        # =====================================

        post_link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.message_id}"

        # =====================================
        # AUTO KOMENTAR
        # =====================================

        komentar = """
🛺 parker auto reply

Ada scammer/rusuh?
Tag @admin atau /report 3x

Open paid promote
Check @parkerinfo
"""

        bot.send_message(
            DISCUSSION_GROUP_ID,
            komentar
        )

        # =====================================
        # NOTIF USER
        # =====================================

        bot.reply_to(
            message,
            f"""
✅ Foto berhasil terkirim

📦 Sisa limit:
{sisa}/35

🔗 Link menfess:
{post_link}
"""
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
