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
    "✨ Sab kuch samay par hota hai"
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
        "🤖 Commands:\n/start\n/help\n/users\n\nTry:\nhello\ntime\ndate\ncoins\nearn\njoke\nmotivation\nspiritual\nmy name is Abhi"
    )

# =========================
# 🔹 USERS COUNT
# =========================

async def users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👥 Total users: {len(users)}")

# =========================
# 🔹 LANGUAGE DETECT
# =========================

def detect_language(text):
    text = text.lower()

    if any(x in text for x in ["ki korcho", "kemon", "bhalo", "tumi", "amar"]):
        return "bn"
    elif any(x in text for x in ["kya", "kaise", "tum", "mera"]):
        return "hi"
    else:
        return "en"

# =========================
# 🔹 INTENT DETECT
# =========================

def detect_intent(text):
    text = text.lower()

    if any(x in text for x in ["hello", "hi", "hey", "namaste", "nomoskar"]):
        return "greet"

    if "time" in text:
        return "time"

    if "date" in text:
        return "date"

    if "coin" in text:
        return "coins"

    if "earn" in text:
        return "earn"

    if any(x in text for x in ["name", "naam", "nam"]):
        return "name"

    if any(x in text for x in ["joke", "funny", "maja"]):
        return "joke"

    if any(x in text for x in ["motivate", "motivation", "inspire"]):
        return "motivation"

    if any(x in text for x in ["bhagwan", "god", "krishna", "ram"]):
        return "spiritual"

    return "chat"

# =========================
# 🔹 REPLY SYSTEM
# =========================

def get_reply(text, user_id):
    intent = detect_intent(text)
    lang = detect_language(text)
    name = names.get(user_id, "")

    # GREET
    if intent == "greet":
        if lang == "bn":
            return f"Nomoskar {name} 😊" if name else "Nomoskar 😊"
        elif lang == "hi":
            return f"Namaste {name} 🙏" if name else "Namaste 🙏"
        else:
            return f"Hello {name} 😄" if name else "Hello 😄"

    # HOW ARE YOU
    if "how are you" in text.lower() or "kaise ho" in text.lower():
        return f"Main theek hu {name} 😄 tum batao?" if name else "Main mast hu 😄 tum batao?"

    # TIME
    elif intent == "time":
        return "⏰ " + datetime.now(india).strftime("%H:%M:%S")

    # DATE
    elif intent == "date":
        return "📅 " + datetime.now(india).strftime("%d-%m-%Y")

    # COINS
    elif intent == "coins":
        return f"💰 {name}, coins: {coins.get(user_id, 0)}" if name else f"💰 Coins: {coins.get(user_id, 0)}"

    # EARN
    elif intent == "earn":
        return f"💸 Earn coins:\nhttps://t.me/YOUR_BOT?start={user_id}"

    # NAME SAVE
    elif "my name is" in text or "mera naam" in text or "amar nam" in text:
        name_input = text.lower().replace("my name is", "").replace("mera naam", "").replace("amar nam", "").strip()
        if name_input:
            names[user_id] = name_input
            return f"Nice to meet you {name_input} 😄"

    # NAME CHECK
    elif intent == "name":
        return names.get(user_id, "Naam nahi bataya 🤔")

    # JOKE
    elif intent == "joke":
        return random.choice(jokes_list)

    # MOTIVATION
    elif intent == "motivation":
        return random.choice(motivation_list)

    # SPIRITUAL
    elif intent == "spiritual":
        return random.choice(spiritual_list)

    # DEFAULT CHAT
    else:
        if lang == "bn":
            return random.choice([
                "Bujhte parchi na 🤔 aro bolo",
                "Valo 😊 kotha bolo",
                "Interesting 🔥"
            ])
        elif lang == "hi":
            return random.choice([
                "Samajh nahi aaya 🤔 thoda aur bolo",
                "Acha 😄 aur batao",
                "Interesting 🔥"
            ])
        else:
            return random.choice([
                "I didn't get it 🤔 say more",
                "Interesting 😄 tell more",
                "Nice 🔥"
            ])

# =========================
# 🔹 TYPING EFFECT
# =========================

async def send_typing(update):
    await update.message.chat.send_action(action=ChatAction.TYPING)
    await asyncio.sleep(random.uniform(1, 2.5))

# =========================
# 🔹 SAVE CHAT
# =========================

def save_chat(user_id, user_text, bot_reply):
    with open("chat_log.txt", "a") as f:
        f.write(f"{user_id} | You: {user_text} | Bot: {bot_reply}\n")

# =========================
# 🔹 HANDLE MESSAGE
# =========================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id
    users.add(user_id)

    # anti spam
    now = datetime.now().timestamp()
    if user_id in last_msg and now - last_msg[user_id] < 1.5:
        return
    last_msg[user_id] = now

    coins[user_id] = coins.get(user_id, 0) + 1

    await send_typing(update)

    reply = get_reply(user_text, user_id)

    save_chat(user_id, user_text, reply)

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
