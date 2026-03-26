from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio, random, os

TOKEN = os.getenv("TOKEN")

user_mode = {}
memory = {}

# ===== typing effect =====
async def send(update, text):
    await update.message.chat.send_action(action="typing")
    await asyncio.sleep(0.4)
    await update.message.reply_text(text)

# ===== START MENU =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send(update,
    "🔥 MENU 🔥\n\n"
    "1 Chat 💬\n"
    "2 Calculator 🔢\n"
    "3 Daily Life 🧠\n"
    "4 Health 💪\n"
    "5 Study 📚\n"
    "6 Earning 💰\n"
    "7 YouTube 🎬\n"
    "8 Editing ✂️\n\n"
    "👉 number bhejo")

# ===== CHAT SYSTEM (FULL SAME LOGIC) =====
async def chat_system(update, text, uid):

    if text in ["hi","hello","hey"]:
        await send(update,"hello")

    elif "my name" in text:
        name = text.replace("my name","").strip()
        memory.setdefault(uid,{})["name"] = name
        await send(update,f"hello {name}")

    elif text == "what is my name":
        await send(update, memory.get(uid,{}).get("name","None"))

    elif "my city" in text:
        city = text.replace("my city","").strip()
        memory.setdefault(uid,{})["city"] = city
        await send(update,"city saved ✔")

    elif text == "what is my city":
        await send(update, memory.get(uid,{}).get("city","None"))

    # ===== CALCULATOR SYSTEM (FULL) =====
async def calc_system(update, text):

    try:
        # ===== BASIC OPERATIONS =====
        if any(op in text for op in ["+","-","*","/","%","**"]):
            result = eval(text)
            await send(update,f"Result = {result}")

        # ===== EVEN / ODD =====
        elif text.startswith("even"):
            num = int(text.split()[-1])
            if num % 2 == 0:
                await send(update,f"{num} EVEN hai")
            else:
                await send(update,f"{num} ODD hai")

        # ===== FACTORIAL =====
        elif text.startswith("fact"):
            num = int(text.split()[-1])
            if num < 0:
                await send(update,"Factorial not possible")
            else:
                fact = 1
                for i in range(1, num+1):
                    fact *= i
                await send(update,f"Factorial = {fact}")

        # ===== POWER =====
        elif text.startswith("power"):
            parts = text.split()
            num1 = int(parts[1])
            num2 = int(parts[2])
            await send(update,f"Power = {num1**num2}")

        # ===== MODULUS =====
        elif text.startswith("mod"):
            parts = text.split()
            num1 = int(parts[1])
            num2 = int(parts[2])
            if num2 == 0:
                await send(update,"cannot divide by zero")
            else:
                await send(update,f"Modulus = {num1 % num2}")

        # ===== AVERAGE =====
        elif text.startswith("avg"):
            nums = list(map(int, text.split()[1:]))
            avg = sum(nums)/len(nums)
            await send(update,f"Average = {round(avg,2)}")

        # ===== WEIGHTED AVERAGE =====
        elif text.startswith("wavg"):
            parts = list(map(int,text.split()[1:]))
            values = parts[::2]
            weights = parts[1::2]

            total = sum(v*w for v,w in zip(values,weights))
            total_w = sum(weights)

            if total_w == 0:
                await send(update,"Weight zero nahi ho sakta")
            else:
                result = total/total_w
                await send(update,f"Weighted Average = {round(result,2)}")

        # ===== GCD / LCM =====
        elif text.startswith("gcd"):
            a,b = map(int,text.split()[1:3])
            x,y = a,b
            while y:
                x,y = y,x%y
            gcd = x
            lcm = (a*b)//gcd
            await send(update,f"GCD = {gcd}\nLCM = {lcm}")

        # ===== PRIME =====
        elif text.startswith("prime"):
            num = int(text.split()[-1])

            if num <= 1:
                await send(update,"Not Prime")
            else:
                is_prime = True
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        is_prime=False
                        break

                await send(update,"Prime" if is_prime else "Not Prime")

        # ===== FACTORS =====
        elif text.startswith("factors"):
            num = int(text.split()[-1])
            factors = []

            for i in range(1,int(num**0.5)+1):
                if num%i==0:
                    factors.append(i)
                    if i != num//i:
                        factors.append(num//i)

            factors.sort()
            await send(update,f"Factors: {factors}")

        # ===== PERCENTAGE BASIC =====
        elif text.startswith("percent"):
            parts = list(map(int,text.split()[1:]))
            total, part = parts
            percent = (part/total)*100
            await send(update,f"{round(percent,2)}%")

        else:
            await send(update,
            "Examples:\n"
            "5+3\n"
            "fact 5\n"
            "even 4\n"
            "power 2 3\n"
            "avg 1 2 3\n"
            "gcd 10 20\n"
            "prime 7\n"
            "factors 12")

    except:
        await send(update,"Invalid input ❌")

    elif text in ["how are you","kaise ho","kemon acho","kaisi ho","valo acho"]:
        await send(update,"fine and you")

    elif text in ["by","bye","tc","tata"]:
        await send(update,"by friend fir milenge")

    elif "kaise ho" in text:
        await send(update,"main badhiya hu 😎 tum batao")

    elif "kya kar rahe ho" in text:
        await send(update,"tumse baat kar raha hu 😄")

    elif "tum kaun ho" in text:
        await send(update,"main ek smart python bot hu 💀")

    elif "help" in text:
        replies = [
            "what problem dear🤔",
            "kya chahiye tumhe🙄",
            "help kya chahiye tymhe 🤔"
        ]
        await send(update, random.choice(replies))

    else:
        replies = [
            "thoda aur clear bolo 🤔",
            "samajhne ki koshish kar raha hu 😅",
            "ye thoda alag hai, fir bolo 😄",
            "samajh nahi aaya, simple bolo 😎"
        ]
        await send(update, random.choice(replies))


# ===== DAILY LIFE SYSTEM =====
async def life_system(update, text):

    if any(word in text for word in ["student","study","padhai"]):
        await send(update,
        "🎓 STUDENT MODE\n\n"
        "⏰ 5:30 AM - Utho\n"
        "🧘 Meditation\n"
        "📚 Hard subject\n"
        "🔁 Revision\n"
        "🏃 Exercise\n"
        "🌙 Sleep\n\n"
        "👉 Consistency > Motivation")

    elif any(word in text for word in ["business","work","job"]):
        await send(update,
        "💼 BUSINESS MODE\n\n"
        "⏰ Early wake\n"
        "📊 Planning\n"
        "📞 Work\n"
        "📈 Growth\n"
        "💡 Learning\n\n"
        "👉 Income = Skill × Consistency")

    elif "morning" in text:
        await send(update,
        "🌅 MORNING ROUTINE\n"
        "👉 Utho\n👉 Pani\n👉 Exercise\n👉 Meditation\n👉 Plan")

    elif "night" in text:
        await send(update,
        "🌙 NIGHT ROUTINE\n"
        "👉 Phone band\n👉 Review\n👉 Plan\n👉 Gratitude\n👉 Sleep")

    elif any(word in text for word in ["bore","bored"]):
        await send(update,
        "😐 Bored?\n👉 Walk\n👉 Music\n👉 Learn something\n\n👉 Growth signal")

    elif any(word in text for word in ["sad","dukhi","mood off"]):
        await send(update,
        "😔 Temporary hai\n👉 Walk\n👉 Breathe\n👉 Talk\n\n👉 Tum strong ho 💪")

    elif "focus" in text:
        await send(update,
        "🎯 Focus Mode\n👉 Phone door\n👉 25 min\n👉 Single task")

    elif any(word in text for word in ["motivation","lazy"]):
        await send(update,
        "🔥 Discipline > Motivation\n👉 Daily improve")

    elif "tired" in text:
        await send(update,
        "😴 Rest lo\n👉 Water\n👉 Relax")

    elif "help" in text:
        await send(update,
        "Commands:\nstudent\nbusiness\nmorning\nnight\nbored\nsad\nfocus")

    else:
        await send(update,"Samajh nahi aaya 🤖")


# ===== HEALTH SYSTEM =====
async def health_system(update, text):

    if any(word in text for word in ["weight loss","fat","motapa"]):
        await send(update,
        "🔥 Weight Loss\n🏃 Walk\n🥗 Diet\n💧 Water\n👉 Consistency")

    elif any(word in text for word in ["weight gain","patla"]):
        await send(update,
        "💪 Weight Gain\n🍌 Banana\n🥛 Milk\n🍚 High calories")

    elif any(word in text for word in ["home","ghar"]):
        await send(update,
        "🏠 Home Workout\n👉 Pushup\n👉 Squat\n👉 Plank")

    elif "gym" in text:
        await send(update,
        "🏋 Gym\n👉 Split workout\n👉 Protein\n👉 Form")

    elif any(word in text for word in ["yoga","meditation"]):
        await send(update,
        "🧘 Yoga\n👉 Pranayam\n👉 Breathing\n👉 Calm mind")

    elif any(word in text for word in ["diet","food"]):
        await send(update,
        "🥗 Diet\n👉 Protein\n👉 Fruits\n👉 Less junk")

    elif "help" in text:
        await send(update,
        "Commands:\nweight loss\ngain\nhome\ngym\nyoga\ndiet")

    else:
        await send(update,"Healthy raho 💪")


        # ===== STUDY SYSTEM =====
async def study_system(update, text):

    if any(word in text for word in ["focus","padhai","study"]):
        await send(update,
        "🎯 FOCUS MODE\n\n"
        "👉 Phone door\n"
        "👉 25 min (Pomodoro)\n"
        "👉 Ek subject\n"
        "👉 Break\n\n"
        "👉 Deep work = success")

    elif any(word in text for word in ["exam","test","paper"]):
        await send(update,
        "📝 EXAM MODE\n\n"
        "👉 Important topics\n"
        "👉 PYQ solve\n"
        "👉 Time manage\n\n"
        "👉 Smart study > Hard")

    elif any(word in text for word in ["revision","revise"]):
        await send(update,
        "🔁 REVISION\n\n"
        "👉 1 din baad\n"
        "👉 3 din baad\n"
        "👉 7 din baad\n\n"
        "👉 Repeat = memory strong")

    elif any(word in text for word in ["time table","routine","plan"]):
        await send(update,
        "⏰ TIME TABLE\n\n"
        "5:30 Wake\n"
        "6–8 Hard subject\n"
        "10–1 Study\n"
        "4–6 Revision\n"
        "10 Sleep")

    elif any(word in text for word in ["motivation","lazy"]):
        await send(update,
        "🔥 STUDY MOTIVATION\n\n"
        "👉 Aaj padhoge kal jeetoge\n"
        "👉 Discipline > Mood")

    elif any(word in text for word in ["math","science","english"]):
        await send(update,
        "📖 SUBJECT\n\n"
        "Math → Practice\n"
        "Science → Concept\n"
        "English → Reading")

    elif "help" in text:
        await send(update,
        "Commands:\nfocus\nexam\nrevision\ntime table\nmotivation")

    else:
        await send(update,"Study karo 📚")


# ===== EARNING SYSTEM =====
async def earning_system(update, text):

    if any(word in text for word in ["start","beginner"]):
        await send(update,
        "🚀 START EARNING\n\n"
        "👉 Skill sikho\n"
        "👉 Daily kaam\n"
        "👉 Free tools\n\n"
        "👉 Skill = money")

    elif any(word in text for word in ["freelance","client"]):
        await send(update,
        "💻 FREELANCING\n\n"
        "👉 Fiverr\n"
        "👉 Upwork\n"
        "👉 Small start")

    elif "youtube" in text:
        await send(update,
        "🎬 YOUTUBE\n\n"
        "👉 Daily upload\n"
        "👉 Shorts + long\n"
        "👉 Consistency")

    elif any(word in text for word in ["affiliate","product"]):
        await send(update,
        "🛒 AFFILIATE\n\n"
        "👉 Product sell\n"
        "👉 Link share\n"
        "👉 Commission")

    elif any(word in text for word in ["content","reel","shorts"]):
        await send(update,
        "📱 CONTENT\n\n"
        "👉 Reels banao\n"
        "👉 Trending use\n"
        "👉 Daily post")

    elif any(word in text for word in ["skill","coding","editing"]):
        await send(update,
        "🧠 SKILL\n\n"
        "👉 Coding\n"
        "👉 Editing\n"
        "👉 Design\n\n"
        "👉 High skill = high income")

    elif any(word in text for word in ["mindset","lazy"]):
        await send(update,
        "🧠 MINDSET\n\n"
        "👉 Consistency\n"
        "👉 Daily work\n"
        "👉 Patience\n\n"
        "👉 6 mahine me result")

    elif "help" in text:
        await send(update,
        "Commands:\nstart\nfreelance\nyoutube\naffiliate\ncontent\nskill")

    else:
        await send(update,"Earn karna hai to skill build karo 💰")

# ===== YOUTUBE SYSTEM =====
async def yt_system(update, text):

    if any(word in text for word in ["start","channel","begin"]):
        await send(update,
        "🚀 START YOUTUBE\n\n"
        "👉 Niche choose karo\n"
        "👉 Daily upload\n"
        "👉 Overthinking mat karo\n\n"
        "👉 Start fast")

    elif any(word in text for word in ["shorts","reel"]):
        await send(update,
        "🔥 SHORTS\n\n"
        "👉 10–20 sec\n"
        "👉 Hook strong\n"
        "👉 Fast edit\n\n"
        "👉 Fast growth")

    elif any(word in text for word in ["viral","views"]):
        await send(update,
        "💀 VIRAL\n\n"
        "👉 Hook + Emotion\n"
        "👉 Trend use\n"
        "👉 Repeat content")

    elif any(word in text for word in ["edit","editing"]):
        await send(update,
        "✂️ EDITING\n\n"
        "👉 Fast cuts\n"
        "👉 Text\n"
        "👉 Sound\n\n"
        "👉 Retention boost")

    elif any(word in text for word in ["title","thumbnail"]):
        await send(update,
        "🧲 TITLE + THUMB\n\n"
        "👉 Curiosity\n"
        "👉 Numbers\n"
        "👉 Simple")

    elif any(word in text for word in ["grow","subscriber"]):
        await send(update,
        "📈 GROWTH\n\n"
        "👉 Consistency\n"
        "👉 Quality\n"
        "👉 Patience\n\n"
        "👉 100 video rule")

    elif "help" in text:
        await send(update,
        "Commands:\nstart\nshorts\nviral\nediting\ntitle\ngrowth")

    else:
        await send(update,"YouTube pe consistency rakho 🎬")


# ===== EDITING SYSTEM =====
async def edit_system(update, text):

    if any(word in text for word in ["basic","start"]):
        await send(update,
        "🎬 BASIC EDITING\n\n"
        "👉 Cut\n"
        "👉 Trim\n"
        "👉 Simple text\n\n"
        "👉 Clean video best")

    elif any(word in text for word in ["shorts","reel"]):
        await send(update,
        "🔥 SHORTS EDIT\n\n"
        "👉 Fast cuts\n"
        "👉 Zoom\n"
        "👉 Subtitle\n\n"
        "👉 Hook first")

    elif any(word in text for word in ["advanced","pro"]):
        await send(update,
        "🎥 ADVANCED\n\n"
        "👉 Transition\n"
        "👉 Motion\n"
        "👉 Slowmo")

    elif any(word in text for word in ["text","subtitle"]):
        await send(update,
        "📝 TEXT\n\n"
        "👉 Bold\n"
        "👉 Short line\n"
        "👉 Highlight")

    elif any(word in text for word in ["sound","music"]):
        await send(update,
        "🔊 SOUND\n\n"
        "👉 Music\n"
        "👉 Effect\n"
        "👉 Beat sync")

    elif any(word in text for word in ["color","filter"]):
        await send(update,
        "🎨 COLOR\n\n"
        "👉 Brightness\n"
        "👉 Contrast\n"
        "👉 Natural look")

    elif "help" in text:
        await send(update,
        "Commands:\nbasic\nshorts\nadvanced\ntext\nsound\ncolor")

    else:
        await send(update,"Editing improve karo ✂️")

# ===== MAIN HANDLER =====
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id
    text = update.message.text.lower()

    modes = {
        "1":"chat",
        "2":"calc",
        "3":"life",
        "4":"health",
        "5":"study",
        "6":"earn",
        "7":"yt",
        "8":"edit"
    }

    # ===== MODE SELECT =====
    if text in modes:
        user_mode[uid] = modes[text]
        return await send(update, f"✅ {modes[text]} mode ON")

    mode = user_mode.get(uid)

    # ===== ROUTING =====
    if mode == "chat":
        await chat_system(update, text, uid)

    elif mode == "calc":
        await calc_system(update, text)

    elif mode == "life":
        await life_system(update, text)

    elif mode == "health":
        await health_system(update, text)

    elif mode == "study":
        await study_system(update, text)

    elif mode == "earn":
        await earning_system(update, text)

    elif mode == "yt":
        await yt_system(update, text)

    elif mode == "edit":
        await edit_system(update, text)

    else:
        await send(update, "👉 /start likho pehle")


# ===== RUN BOT =====
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

print("✅ BOT RUNNING...")
app.run_polling()
