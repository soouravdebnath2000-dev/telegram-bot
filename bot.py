import os
import random
import asyncio
from datetime import datetime
import pytz

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ChatAction

TOKEN = os.getenv("TOKEN")

# 🧠 DATA
users = set()
coins = {}
names = {}
last_msg = {}

india = pytz.timezone("Asia/Kolkata")

# =========================
# 🔹 EXTRA DATA
# =========================

jokes_list = [
    "😂 Coding itni ki zindagi bhi compile nahi ho rahi",
    "🤣 Doctor: Tumhe kya problem hai?\nPatient: Paisa nahi hai 😭",
    "😄 Network gaya = life gaya"
]

motivation_list = [
    "🔥 Mehnat kabhi bekaar nahi jaati",
    "🚀 Aaj seekhoge, kal jeetoge",
    "💪 Discipline = Power"
]

spiritual_list = [
    "🕉️ Jo tum dhoond rahe ho, wo tumhare andar hai",
    "🙏 Shanti mann se aati hai, duniya se nahi",
    "✨ Sab kuch samay par hota hai",
    "🌿 Bhagwan par bharosa rakho, sab theek hoga"
]

# =========================
# 🔹 START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    users.add(user_id)

    if user_id not in coins:
        coins[user_id] = 10

    await update.message.reply_text(
        f"👋 Welcome!\n💰 Coins: {coins[user_id]}\n\nType anything to chat 😄"
    )

# =========================
# 🔹 HELP
# =========================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands:\n/start\n/help\n/users\n\nTry:\nhello\ntime\ndate\ncoins\nearn\njoke\nmotivation\nspiritual\nshayari\nlove you\nmy name is Abhi"
    )

# =========================
# 🔹 USERS COUNT
# =========================

async def users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👥 Total users: {len(users)}")

# =========================
# 🔹 INTENT DETECT
# =========================

def detect_intent(text):
    text = text.lower()

    if any(x in text for x in ["hello", "hi", "hey", "namaste"]):
        return "greet"

    if "time" in text:
        return "time"

    if "date" in text:
        return "date"

    if "coin" in text:
        return "coins"

    if "earn" in text:
        return "earn"

    if any(x in text for x in ["name", "naam"]):
        return "name"

    if any(x in text for x in ["joke", "funny"]):
        return "joke"

    if any(x in text for x in ["motivation", "inspire"]):
        return "motivation"

    if any(x in text for x in ["bhagwan", "god"]):
        return "spiritual"

    return "chat"

# =========================
# 🔹 REPLY SYSTEM (FINAL 🔥)
# =========================

def get_reply(text, user_id):
    text_lower = text.lower()
    intent = detect_intent(text)
    name = names.get(user_id, "")

    # ❤️ LOVE
    if "love you" in text_lower:
        return random.choice([
            f"Love you too {name} ❤️" if name else "Love you too ❤️",
            "Aree ❤️ itna pyaar 😄",
            "Dil jeet liya tumne ❤️🔥"
        ])

    # ✍️ SHAYARI
    elif "shayari" in text_lower:
        return random.choice([
            "💫 Zindagi ek kahani hai,\nHar pal ek nayi nishani hai…",
            "❤️ Dil se jo baat nikalti hai,\nWo hi asli shayari hoti hai…",
            "🌙 Raat bhi kya khoob hai,\nTeri yaadon ke saath mehfooz hai…"
        ])

    # 👋 GREET
    elif intent == "greet":
        return random.choice([
            f"Hello {name} 😄 kaise ho?" if name else "Hello 😄 kaise ho?",
            f"Namaste {name} 🙏 kya help chahiye?" if name else "Namaste 🙏 kya help chahiye?",
            "Hey 🔥 kya chal raha hai?"
        ])

    # 😊 HOW ARE YOU
    elif "kaise ho" in text_lower:
        return random.choice([
            f"Main mast hu {name} 😄 tum batao?" if name else "Main mast hu 😄 tum batao?",
            "Sab badhiya 😎 tum sunao?",
            "Zindagi chal rahi hai 🔥 tum batao?"
        ])

    # 🤖 BOT INTRO
    elif "tum kya kar sakte ho" in text_lower:
        return """🤖 Main ek smart bot hu:

✔ Time / Date  
✔ Jokes 😄  
✔ Motivation 🚀  
✔ Spiritual baate 🕉️  
✔ Shayari ✍️  
✔ Naam yaad rakh sakta hu  

Aur bhi seekh raha hu 🔥"""

    # ⏰ TIME
    elif intent == "time":
        return "⏰ " + datetime.now(india).strftime("%H:%M:%S")

    # 📅 DATE
    elif intent == "date":
        return "📅 " + datetime.now(india).strftime("%d-%m-%Y")

    # 💰 COINS
    elif intent == "coins":
        return f"💰 {name}, coins: {coins.get(user_id, 0)}" if name else f"💰 Coins: {coins.get(user_id, 0)}"

    # 💸 EARN
    elif intent == "earn":
        return f"💸 Earn coins:\nhttps://t.me/YOUR_BOT?start={user_id}"

    # 🧠 NAME SAVE
    elif "my name is" in text_lower or "mera naam" in text_lower:
        name_input = text_lower.replace("my name is", "").replace("mera naam", "").replace("hai","").strip()
        if name_input:
            names[user_id] = name_input
            return f"Nice to meet you {name_input} 😄"

    # 🧠 NAME CHECK
    elif intent == "name":
        return names.get(user_id, "Naam nahi bataya 🤔")

    # 😂 JOKE
    elif intent == "joke":
        return random.choice(jokes_list)

    # 🚀 MOTIVATION
    elif intent == "motivation":
        return random.choice(motivation_list)

    # 🕉️ SPIRITUAL
    elif intent == "spiritual":
        return random.choice(spiritual_list)

    # 🔥 DEFAULT
    else:
        return random.choice([
            "🤖 Samajhne ki koshish kar raha hu… thoda aur bolo 🔥",
            "Interesting 😄 aur batao",
            "Try karo: joke / motivation / shayari 😎",
            "Main seekh raha hu 😄"
        ])

# =========================
# 🔹 TYPING EFFECT
# =========================

async def send_typing(update):
    await update.message.chat.send_action(action=ChatAction.TYPING)
    await asyncio.sleep(random.uniform(1, 2.5))

# =========================
# 🔹 HANDLE MESSAGE
# =========================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id
    users.add(user_id)

    now = datetime.now().timestamp()
    if user_id in last_msg and now - last_msg[user_id] < 1.5:
        return
    last_msg[user_id] = now

    coins[user_id] = coins.get(user_id, 0) + 1

    await send_typing(update)

    reply = get_reply(user_text, user_id)

    await update.message.reply_text(reply)

# =========================
# 🔹 MAIN
# =========================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("users", users_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🔥 PRO BOT RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()
