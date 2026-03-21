import os
import random
from datetime import datetime
import pytz

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 TOKEN
TOKEN = os.getenv("TOKEN")

# 🧠 DATA STORAGE
users = set()
coins = {}
names = {}

# 🌍 TIMEZONE
india = pytz.timezone("Asia/Kolkata")

# =========================
# 🔹 BASIC COMMANDS
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    users.add(user_id)

    # 💰 init coins
    if user_id not in coins:
        coins[user_id] = 0

    # 🎯 referral system
    if context.args:
        try:
            ref_id = int(context.args[0])
            if ref_id != user_id:
                coins[ref_id] = coins.get(ref_id, 0) + 5
        except:
            pass

    await update.message.reply_text(
        f"👋 Welcome!\nCoins: {coins[user_id]} 💰\nType 'earn' to earn coins"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\n/help\n\nTry:\nhello\ntime\ndate\ncoins\nearn"
    )

# =========================
# 🔹 MAIN CHAT LOGIC
# =========================

def get_reply(text, user_id):
    text = text.lower()

    # 🌍 MULTI LANGUAGE
    if any(x in text for x in ["hi", "hello", "hey", "namaste", "nomoskar"]):
        return random.choice(["Hello 😄", "Namaste 🙏", "Nomoskar 😊"])

    elif any(x in text for x in ["kaise ho", "how are you", "kemon acho"]):
        return random.choice(["Main mast hu 😎", "Bhalo achi 😄"])

    # ⏰ TIME
    elif "time" in text:
        return "⏰ " + datetime.now(india).strftime("%H:%M")

    # 📅 DATE
    elif "date" in text:
        return "📅 " + datetime.now(india).strftime("%d-%m-%Y")

    # 💰 COINS
    elif "coins" in text:
        return f"💰 Coins: {coins.get(user_id, 0)}"

    # 💸 EARN
    elif "earn" in text:
        return f"Referral link:\nhttps://t.me/darkcoder_abhi_bot?start={user_id}"

    # 🧠 NAME SAVE
    elif "mera naam" in text or "my name" in text or "amar nam" in text:
        name = text.replace("mera naam", "").replace("my name", "").replace("amar nam", "").strip()
        if name:
            names[user_id] = name
            return f"Nice to meet you {name} 😄"
        else:
            return "Apna naam batao 😄"

    # 🧠 NAME CHECK
    elif "mera naam kya" in text or "my name" in text:
        return names.get(user_id, "Tumne naam nahi bataya 🤔")

    # 📊 USERS
    elif "kitne log" in text:
        return f"{len(users)} users use kar rahe hain 😎"

    # 🤖 DEFAULT
    return random.choice([
        "Samajh nahi aaya 🤔",
        "Acha 😄",
        "Nice 😎",
        "Aur bolo 🔥"
    ])

# =========================
# 🔹 MESSAGE HANDLER
# =========================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id

    reply = get_reply(user_text, user_id)
    await update.message.reply_text(reply)

# =========================
# 🔹 MAIN
# =========================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🔥 Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
