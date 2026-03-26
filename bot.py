# ===== PART 1: BASE SYSTEM =====

import telebot
import time
import random

TOKEN = "8715453613:AAH-exdCVPtYFbdmWbobu7Du8C-AA5Q18p0"

bot = telebot.TeleBot(TOKEN)

memory = {}

# ===== TYPING EFFECT =====
def typing(chat_id, text):
    bot.send_chat_action(chat_id, "typing")
    time.sleep(1)
    bot.send_message(chat_id, text)

# ===== START =====
@bot.message_handler(commands=['start'])
def start(msg):
    typing(msg.chat.id, "🔥 Welcome Gurudev\nType /help")

# ===== HELP =====
@bot.message_handler(commands=['help'])
def help_cmd(msg):
    typing(msg.chat.id,
    "📌 Commands:\n"
    "/chat - Smart Chat\n"
    "/calc - Calculator\n"
    "/daily - Daily Life\n"
    "/fitness - Health\n"
    "/study - Study Help\n"
    "/earn - Online Earning\n"
    "/youtube - Growth\n"
    "/edit - Editing System"
    )

# ===== CHAT SYSTEM =====
@bot.message_handler(commands=['chat'])
def chat_start(msg):
    typing(msg.chat.id, "💬 Chat Mode ON\nType anything...")

# ===== MAIN MESSAGE HANDLER =====
@bot.message_handler(func=lambda message: True)
def handle(msg):
    text = msg.text.lower()
    chat_id = msg.chat.id

    # ===== CHAT LOGIC =====
    if text in ["hi", "hello", "hey"]:
        typing(chat_id, "hello 😎")

    elif "my name" in text:
        name = text.replace("my name", "").strip()
        memory[chat_id] = {"name": name}
        typing(chat_id, f"hello {name}")

    elif text == "what is my name":
        name = memory.get(chat_id, {}).get("name", "unknown")
        typing(chat_id, f"your name is {name}")

    elif text in ["how are you", "kaise ho", "kemon acho"]:
        typing(chat_id, "fine and you 😄")

    elif text in ["bye", "tata", "tc"]:
        typing(chat_id, "bye friend 👋")

    elif "help" in text:
        replies = ["kya chahiye 🤔", "bolo kya problem", "kaise help karu"]
        typing(chat_id, random.choice(replies))

    else:
        replies = [
            "samajh nahi aaya 😅",
            "simple bolo 😎",
            "thoda clear karo 🤔"
        ]
        typing(chat_id, random.choice(replies))


# ===== RUN =====
print("BOT RUNNING...")
bot.infinity_polling()

# ===== PART 2: CALCULATOR SYSTEM =====

def calc_menu():
    return (
        "🧮 Calculator Commands:\n"
        "/add 5 6\n"
        "/sub 10 3\n"
        "/mul 4 5\n"
        "/div 10 2\n"
        "/square 5\n"
        "/cube 3\n"
        "/power 2 5\n"
        "/mod 10 3\n"
        "/even 8\n"
        "/percent 200 10\n"
    )

@bot.message_handler(commands=['calc'])
def calc_start(msg):
    typing(msg.chat.id, calc_menu())


# ===== ADD =====
@bot.message_handler(commands=['add'])
def add_cmd(msg):
    try:
        _, a, b = msg.text.split()
        result = int(a) + int(b)
        typing(msg.chat.id, f"Add = {result}")
    except:
        typing(msg.chat.id, "Format: /add 5 6")


# ===== SUBTRACT =====
@bot.message_handler(commands=['sub'])
def sub_cmd(msg):
    try:
        _, a, b = msg.text.split()
        result = int(a) - int(b)
        typing(msg.chat.id, f"Subtract = {result}")
    except:
        typing(msg.chat.id, "Format: /sub 10 3")


# ===== MULTIPLY =====
@bot.message_handler(commands=['mul'])
def mul_cmd(msg):
    try:
        _, a, b = msg.text.split()
        result = int(a) * int(b)
        typing(msg.chat.id, f"Multiply = {result}")
    except:
        typing(msg.chat.id, "Format: /mul 4 5")


# ===== DIVIDE =====
@bot.message_handler(commands=['div'])
def div_cmd(msg):
    try:
        _, a, b = msg.text.split()
        if int(b) == 0:
            typing(msg.chat.id, "Cannot divide by zero ❌")
        else:
            result = int(a) / int(b)
            typing(msg.chat.id, f"Divide = {result}")
    except:
        typing(msg.chat.id, "Format: /div 10 2")


# ===== SQUARE =====
@bot.message_handler(commands=['square'])
def square_cmd(msg):
    try:
        _, a = msg.text.split()
        result = int(a) ** 2
        typing(msg.chat.id, f"Square = {result}")
    except:
        typing(msg.chat.id, "Format: /square 5")


# ===== CUBE =====
@bot.message_handler(commands=['cube'])
def cube_cmd(msg):
    try:
        _, a = msg.text.split()
        result = int(a) ** 3
        typing(msg.chat.id, f"Cube = {result}")
    except:
        typing(msg.chat.id, "Format: /cube 3")


# ===== POWER =====
@bot.message_handler(commands=['power'])
def power_cmd(msg):
    try:
        _, a, b = msg.text.split()
        result = int(a) ** int(b)
        typing(msg.chat.id, f"Power = {result}")
    except:
        typing(msg.chat.id, "Format: /power 2 5")


# ===== MOD =====
@bot.message_handler(commands=['mod'])
def mod_cmd(msg):
    try:
        _, a, b = msg.text.split()
        result = int(a) % int(b)
        typing(msg.chat.id, f"Modulus = {result}")
    except:
        typing(msg.chat.id, "Format: /mod 10 3")


# ===== EVEN / ODD =====
@bot.message_handler(commands=['even'])
def even_cmd(msg):
    try:
        _, a = msg.text.split()
        num = int(a)
        if num % 2 == 0:
            typing(msg.chat.id, f"{num} EVEN hai")
        else:
            typing(msg.chat.id, f"{num} ODD hai")
    except:
        typing(msg.chat.id, "Format: /even 8")


# ===== PERCENT =====
@bot.message_handler(commands=['percent'])
def percent_cmd(msg):
    try:
        _, total, percent = msg.text.split()
        result = (int(percent) / 100) * int(total)
        typing(msg.chat.id, f"{percent}% of {total} = {result}")
    except:
        typing(msg.chat.id, "Format: /percent 200 10")


# ===== PART 3: PRIME + FACTOR SYSTEM =====

import math
import time


# ===== PRIME =====
@bot.message_handler(commands=['prime'])
def prime_cmd(msg):
    try:
        _, num = msg.text.split()
        num = int(num)

        start_time = time.time()

        steps = []
        factors = []
        is_prime = False

        if num <= 1:
            steps.append("Number 1 ya usse chhota hai")

        elif num == 2:
            is_prime = True
            steps.append("2 eklauta even prime hai")

        elif num % 2 == 0:
            factors.append(2)
            steps.append("Even number hai → 2 se divide hota hai")

        else:
            is_prime = True
            steps.append("Odd number → smart checking start")

            for i in range(3, int(math.sqrt(num)) + 1, 2):
                steps.append(f"{num} % {i} check")

                if num % i == 0:
                    is_prime = False
                    factors.append(i)
                    steps.append(f"{i} se divide ho gaya")
                    break

        end_time = time.time()

        # ===== RESULT =====
        if is_prime:
            result_text = "✅ Prime Number\n👉 kisi bhi number se divide nahi hua"
        else:
            if factors:
                result_text = f"❌ Not Prime\n👉 Factor mila: {factors[0]}"
            else:
                result_text = "❌ Not Prime"

        # ===== STEPS =====
        steps_text = "\n".join(steps[:10])

        final = (
            f"📊 RESULT:\n{result_text}\n\n"
            f"🧠 Steps:\n{steps_text}\n\n"
            f"⏱ Time: {round(end_time - start_time, 6)} sec"
        )

        typing(msg.chat.id, final)

    except:
        typing(msg.chat.id, "Format: /prime 17")


# ===== FACTORS =====
@bot.message_handler(commands=['factors'])
def factors_cmd(msg):
    try:
        _, num = msg.text.split()
        num = int(num)

        factors = []
        pairs = []

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)

                if i != num // i:
                    factors.append(num // i)

                pairs.append((i, num // i))

        factors.sort()

        pair_text = "\n".join([f"{a} × {b} = {num}" for a, b in pairs])

        final = (
            f"📊 Factors: {factors}\n"
            f"👉 Total: {len(factors)}\n\n"
            f"🔗 Pairs:\n{pair_text}"
        )

        typing(msg.chat.id, final)

    except:
        typing(msg.chat.id, "Format: /factors 12")

# ===== PART 4: PERCENTAGE + AVERAGE SYSTEM =====

# ===== PERCENTAGE =====
@bot.message_handler(commands=['percent_full'])
def percent_full(msg):
    try:
        parts = msg.text.split()

        if len(parts) < 2:
            raise Exception

        mode = parts[1]

        # ----- MARKS -----
        if mode == "marks":
            total = int(parts[2])
            obtained = int(parts[3])

            percent = (obtained / total) * 100
            percent = round(percent, 2)

            typing(msg.chat.id, f"📊 Marks = {percent}%")

        # ----- DISCOUNT -----
        elif mode == "discount":
            total = int(parts[2])
            paid = int(parts[3])

            discount = total - paid
            percent = (discount / total) * 100
            percent = round(percent, 2)

            typing(msg.chat.id, f"💸 Discount = {percent}%")

        # ----- PROFIT / LOSS -----
        elif mode == "profit":
            buy = int(parts[2])
            sell = int(parts[3])

            diff = sell - buy
            percent = (abs(diff) / buy) * 100
            percent = round(percent, 2)

            if diff > 0:
                typing(msg.chat.id, f"💰 Profit = {percent}%")
            elif diff < 0:
                typing(msg.chat.id, f"📉 Loss = {percent}%")
            else:
                typing(msg.chat.id, "No profit no loss")

        # ----- DIRECT -----
        elif mode == "direct":
            value = int(parts[2])
            per = int(parts[3])

            result = (per / 100) * value
            typing(msg.chat.id, f"{per}% of {value} = {result}")

        else:
            typing(msg.chat.id, "Invalid mode")

    except:
        typing(msg.chat.id,
        "Format:\n"
        "/percent_full marks 500 400\n"
        "/percent_full discount 1000 800\n"
        "/percent_full profit 100 120\n"
        "/percent_full direct 200 10"
        )


# ===== AVERAGE =====
@bot.message_handler(commands=['average'])
def average_cmd(msg):
    try:
        parts = msg.text.split()

        nums = list(map(int, parts[1:]))

        avg = sum(nums) / len(nums)
        avg = round(avg, 2)

        typing(msg.chat.id, f"📊 Average = {avg}")

    except:
        typing(msg.chat.id, "Format: /average 10 20 30")


# ===== WEIGHTED AVERAGE =====
@bot.message_handler(commands=['wavg'])
def weighted_avg(msg):
    try:
        parts = msg.text.split()

        values = list(map(int, parts[1::2]))
        weights = list(map(int, parts[2::2]))

        total = sum(v * w for v, w in zip(values, weights))
        total_weight = sum(weights)

        if total_weight == 0:
            typing(msg.chat.id, "Weight zero nahi ho sakta ❌")
            return

        result = total / total_weight
        result = round(result, 2)

        typing(msg.chat.id, f"📊 Weighted Average = {result}")

    except:
        typing(msg.chat.id,
        "Format:\n/wavg 10 2 20 3\n(value weight pairs)"
            )

# ===== PART 5: GCD / LCM + ADVANCED MATH =====

import math


# ===== GCD / LCM =====
@bot.message_handler(commands=['gcd'])
def gcd_cmd(msg):
    try:
        _, a, b = msg.text.split()
        a = int(a)
        b = int(b)

        gcd = math.gcd(a, b)

        typing(msg.chat.id, f"🔢 GCD({a}, {b}) = {gcd}")

    except:
        typing(msg.chat.id, "Format: /gcd 12 18")


@bot.message_handler(commands=['lcm'])
def lcm_cmd(msg):
    try:
        _, a, b = msg.text.split()
        a = int(a)
        b = int(b)

        lcm = (a * b) // math.gcd(a, b)

        typing(msg.chat.id, f"🔢 LCM({a}, {b}) = {lcm}")

    except:
        typing(msg.chat.id, "Format: /lcm 12 18")


@bot.message_handler(commands=['gcdlcm'])
def both_cmd(msg):
    try:
        _, a, b = msg.text.split()
        a = int(a)
        b = int(b)

        gcd = math.gcd(a, b)
        lcm = (a * b) // gcd

        typing(msg.chat.id,
        f"🔢 GCD = {gcd}\n🔢 LCM = {lcm}"
        )

    except:
        typing(msg.chat.id, "Format: /gcdlcm 12 18")


# ===== FACTORIAL =====
@bot.message_handler(commands=['fact'])
def fact_cmd(msg):
    try:
        _, n = msg.text.split()
        n = int(n)

        if n < 0:
            typing(msg.chat.id, "Factorial not possible ❌")
            return

        result = math.factorial(n)

        typing(msg.chat.id, f"{n}! = {result}")

    except:
        typing(msg.chat.id, "Format: /fact 5")


# ===== RANGE SUM =====
@bot.message_handler(commands=['sum'])
def sum_cmd(msg):
    try:
        _, a, b = msg.text.split()
        a = int(a)
        b = int(b)

        result = sum(range(a, b + 1))

        typing(msg.chat.id, f"Sum {a} to {b} = {result}")

    except:
        typing(msg.chat.id, "Format: /sum 1 10")


# ===== MULTIPLES =====
@bot.message_handler(commands=['multiples'])
def multiples_cmd(msg):
    try:
        _, num, limit = msg.text.split()
        num = int(num)
        limit = int(limit)

        result = [num * i for i in range(1, limit + 1)]

        typing(msg.chat.id, f"Multiples of {num}:\n{result}")

    except:
        typing(msg.chat.id, "Format: /multiples 5 10")

# ===== PART 6: LIFE SYSTEM =====

# ===== DAILY LIFE =====
@bot.message_handler(commands=['daily'])
def daily_cmd(msg):
    typing(msg.chat.id,
    "🧠 DAILY LIFE SYSTEM\n"
    "Try:\n"
    "student / business / morning / night / sad / focus"
    )


# ===== FITNESS =====
@bot.message_handler(commands=['fitness'])
def fitness_cmd(msg):
    typing(msg.chat.id,
    "💪 FITNESS SYSTEM\n"
    "Try:\n"
    "weight loss / gain / home workout / gym / yoga / diet"
    )


# ===== STUDY =====
@bot.message_handler(commands=['study'])
def study_cmd(msg):
    typing(msg.chat.id,
    "📚 STUDY SYSTEM\n"
    "Try:\n"
    "focus / exam / revision / timetable / motivation"
    )


# ===== EARNING =====
@bot.message_handler(commands=['earn'])
def earn_cmd(msg):
    typing(msg.chat.id,
    "💰 ONLINE EARNING\n"
    "Try:\n"
    "start / freelancing / youtube / affiliate / skill"
    )


# ===== YOUTUBE =====
@bot.message_handler(commands=['youtube'])
def yt_cmd(msg):
    typing(msg.chat.id,
    "🎬 YOUTUBE GROWTH\n"
    "Try:\n"
    "start / shorts / viral / editing / title / growth"
    )


# ===== EDITING =====
@bot.message_handler(commands=['edit'])
def edit_cmd(msg):
    typing(msg.chat.id,
    "✂️ EDITING SYSTEM\n"
    "Try:\n"
    "basic / shorts / advanced / text / sound / color"
    )


# ===== SMART RESPONSE SYSTEM =====
@bot.message_handler(func=lambda msg: True)
def life_handler(msg):
    text = msg.text.lower()
    chat_id = msg.chat.id

    # DAILY LIFE
    if "student" in text:
        typing(chat_id, "🎓 Student Mode:\nConsistency = success 💀")

    elif "business" in text:
        typing(chat_id, "💼 Business Mode:\nSkill + system = income 💰")

    elif "morning" in text:
        typing(chat_id, "🌅 Morning:\nWake up + exercise + plan")

    elif "night" in text:
        typing(chat_id, "🌙 Night:\nReview + plan + sleep")

    elif "sad" in text:
        typing(chat_id, "😔 Relax...\nYe temporary hai 💪")

    elif "focus" in text:
        typing(chat_id, "🎯 Focus:\nPhone door + deep work")

    # FITNESS
    elif "weight loss" in text:
        typing(chat_id, "🔥 Fat loss:\nRun + clean diet")

    elif "gym" in text:
        typing(chat_id, "🏋 Gym:\nConsistency + protein")

    # STUDY
    elif "exam" in text:
        typing(chat_id, "📝 Exam:\nPYQ + revision")

    elif "revision" in text:
        typing(chat_id, "🔁 Repeat = memory strong")

    # EARNING
    elif "freelance" in text:
        typing(chat_id, "💻 Freelancing:\nSkill sell karo")

    elif "youtube" in text:
        typing(chat_id, "🎬 YouTube:\nDaily upload")

    # EDITING
    elif "editing" in text:
        typing(chat_id, "✂️ Editing:\nFast cut + text")

    else:
        typing(chat_id, "🤖 Samajh nahi aaya\nType /help")

# ===== FINAL BOT (PART 7 MERGED) =====

import telebot
import time
import random
import math

TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

memory = {}

# ===== TYPING EFFECT =====
def typing(chat_id, text):
    bot.send_chat_action(chat_id, "typing")
    time.sleep(1)
    bot.send_message(chat_id, text)


# ===== START =====
@bot.message_handler(commands=['start'])
def start(msg):
    typing(msg.chat.id, "🔥 Welcome Gurudev\nType /help")


# ===== HELP =====
@bot.message_handler(commands=['help'])
def help_cmd(msg):
    typing(msg.chat.id,
    "📌 Commands:\n"
    "/chat /calc /prime /factors\n"
    "/percent_full /average /wavg\n"
    "/gcd /lcm /fact /sum /multiples\n"
    "/daily /fitness /study /earn /youtube /edit"
    )


# ===== MAIN HANDLER =====
@bot.message_handler(func=lambda msg: True)
def handle(msg):
    text = msg.text.lower()
    chat_id = msg.chat.id

    # ===== CHAT =====
    if text in ["hi","hello","hey"]:
        typing(chat_id,"hello 😎")

    elif "my name" in text:
        name = text.replace("my name","").strip()
        memory[chat_id] = {"name":name}
        typing(chat_id,f"hello {name}")

    elif text == "what is my name":
        name = memory.get(chat_id,{}).get("name","unknown")
        typing(chat_id,f"your name is {name}")

    # ===== CALCULATOR SHORT =====
    elif text.startswith("/add"):
        try:
            _,a,b = text.split()
            typing(chat_id,f"{int(a)+int(b)}")
        except:
            typing(chat_id,"/add 5 6")

    elif text.startswith("/sub"):
        try:
            _,a,b = text.split()
            typing(chat_id,f"{int(a)-int(b)}")
        except:
            typing(chat_id,"/sub 10 3")

    # ===== PRIME =====
    elif text.startswith("/prime"):
        try:
            _,num = text.split()
            num = int(num)

            if num <= 1:
                typing(chat_id,"Not Prime")
                return

            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0:
                    typing(chat_id,"Not Prime")
                    return

            typing(chat_id,"Prime Number")

        except:
            typing(chat_id,"/prime 17")

    # ===== FACTORS =====
    elif text.startswith("/factors"):
        try:
            _,num = text.split()
            num = int(num)

            fac = [i for i in range(1,num+1) if num%i==0]
            typing(chat_id,str(fac))

        except:
            typing(chat_id,"/factors 12")

    # ===== PERCENT =====
    elif text.startswith("/percent"):
        try:
            _,value,per = text.split()
            result = (int(per)/100)*int(value)
            typing(chat_id,str(result))
        except:
            typing(chat_id,"/percent 200 10")

    # ===== GCD =====
    elif text.startswith("/gcd"):
        try:
            _,a,b = text.split()
            typing(chat_id,str(math.gcd(int(a),int(b))))
        except:
            typing(chat_id,"/gcd 12 18")

    # ===== FACTORIAL =====
    elif text.startswith("/fact"):
        try:
            _,n = text.split()
            typing(chat_id,str(math.factorial(int(n))))
        except:
            typing(chat_id,"/fact 5")

    # ===== LIFE SYSTEM =====
    elif "student" in text:
        typing(chat_id,"🎓 Study hard 💀")

    elif "gym" in text:
        typing(chat_id,"🏋 Gym + diet")

    elif "exam" in text:
        typing(chat_id,"📚 Revision + PYQ")

    elif "youtube" in text:
        typing(chat_id,"🎬 Daily upload")

    else:
        typing(chat_id,"🤖 Unknown command\nType /help")


print("🔥 FINAL BOT RUNNING...")
bot.infinity_polling()
