memory = {}
import random

#chat system
def chat():
    print("💬 chat start" )
    print("type exit to go back\n")
    while True:
        text = input("bolo:").lower()
        
        if text == "exit":
            print("Menu mai aa gaye")
            break
        
        elif text in ["hi","hello","hey"]:
            print("hello")
        
        elif "my name" in text:
            name = text.replace("my name", "").strip()
            memory["name"] = name
            print("hello", name)
            
        elif text == "what is my name":
            print(memory.get("name"))
            
        elif "my city" in text:
            city = text.replace("my city", "").strip()
            memory["city"] = city
            
        elif text == "what is my city":
            print(memory.get("city"))
            
        elif text in ["how are you", "kaise ho", "kemon acho", "kaisi ho", "valo acho"]:
            print("fine and you")
        
        elif text in ["by", "bye", "tc","tata"]:
            print("by friend fir milenge ")
            
        elif "kaise ho" in text:
            print("main badhiya hu 😎 tum batao")

        elif "kya kar rahe ho" in text:
            print("tumse baat kar raha hu 😄")

        elif "tum kaun ho" in text:
            print("main ek smart python bot hu 💀")
        
        elif "help" in text:
            replies = ["what problem dear🤔", "kya chahiye tumhe🙄", "help kya chahiye tymhe 🤔"]
            print(random.choice(replies))
        
        else:
            replies = [
        "thoda aur clear bolo 🤔",
        "samajhne ki koshish kar raha hu 😅",
        "ye thoda alag hai, fir bolo 😄",
        "samajh nahi aaya, simple bolo 😎"
    ]
            print(random.choice(replies))
            

    # calulator smart 

def calculator():
    print("calculator start")
    print("type exit to go back\n")
    
    while True:
        print("1 choice add")
        print("2 choice subtract")
        print("3 choice multiply")
        print("4 choice divide")
        print("5 choise square")
        print("6 choice cube")
        print("7 choice factorial")
        print("8 choice power")
        print("9 choice modulus")
        print("10 choice even/odd")
        print("11 choice percentage")
        print("12 choice average")
        print("13 choice weighted average")
        print("14 choice GCD / LCM")
        print("15 choice Prime Analyzer (steps + factors + time)")
        print("16 choice factors")
        
        op = input("choice operation:")
            
        if op == "exit":
            break
            
        if op in ["1", "2", "3", "4", "8","9"]:
        
            num1 = input("Enter first number:").lower()
            if num1 == "exit":
                break
            
            if not num1.isdigit():
                print("Invalid")
                continue
            num1 = int(num1)
        
            num2 = input("Enter second number:").lower()
            if not num2.isdigit():
                print("Invalid")
                continue
            num2 = int(num2)
        
        elif op in ["5", "6"]:
            num1 = input("Enter number:").lower()
            if not num1.isdigit():
                print("Invalid")
                continue
            num1 = int(num1)

        elif op == "7":
            num = input("Enter number for factorial:").lower()
            if not num.isdigit():
                print("Invalid")
                continue
            num = int(num)
        
        
        if op == "1":
            result = num1 + num2
            print(f"Add Result = {result}")
            with open("history.txt", "a") as f:
                f.write(f"Add: {num1} + {num2} = {result}\n")
            
        elif op == "2":
            result = num1 - num2
            print(f"Subtract Result = {result}")
            
            with open("history.txt", "a") as f:
                f.write(f"Subtract: {num1} - {num2} = {result}\n")
            
        elif op == "3":
            result = num1 * num2
            print(f"Multiply Result = {result}")
            with open("history.txt", "a") as f:
                f.write(f"Multiply: {num1} * {num2} = {result}\n")
        
        elif op == "4":
            if num2 == 0:
                print("cannot divide by zero")
            else:
                result = num1 / num2
                print(f"Divide Result = {result}")
                with open("history.txt", "a") as f:
                    f.write(f"Divide: {num1} / {num2} = {result}\n")
        
        elif op == "5":
            result = num1 ** 2
            print(f"Square = {result}")
            
            with open("history.txt", "a") as f:
                f.write(f"Square: {num1} ** 2 = {result}\n")
                
        elif op == "6":
            result = num1 ** 3
            print(f"Cube = {result}")
            
            with open("history.txt", "a") as f:
                f.write(f"Cube: {num1} ** 3 = {result}\n")
                
        elif op == "7":
            
            
            if num < 0:
                print("Factorial not possible")
            else:
                fact = 1 
                for i in range(1, num + 1):
                    fact = fact * i
                print(f"Factorial = {fact}")
                with open("history.txt", "a") as f:
                    f.write(f"Factorial: {num}! = {fact}\n")
        
        elif op == "8":
            result = num1 ** num2
            print(f"Power = {result}")
            
            with open("history.txt", "a") as f:
                f.write(f"Power: {num1} ** {num2} = {result}\n")
            
        elif op == "9":
            if num2 == 0:
                print("cannot divide by zero")
                continue
            result = num1 % num2
            print(f"Modulus (remainder) = {result}")

            with open("history.txt", "a") as f:
                f.write(f"Modulus: {num1} % {num2} = {result}\n")
        
        elif op == "10":
            num = input("Enter number: ").lower()

            if not num.isdigit():
                print("Invalid")
                continue

            num = int(num)

            if num % 2 == 0:
                print(f"{num} EVEN hai")
            else:
                print(f"{num} ODD hai")
                
            with open("history.txt", "a") as f:
                f.write(f"Even/Odd: {num} -> {'EVEN' if num%2==0 else 'ODD'}\n")       
         
        # new add percentage
        
        elif op == "11":
            print("\n📊 PERCENTAGE SYSTEM")
            print("1 Marks %")
            print("2 Discount %")
            print("3 Profit / loss %")
            print("4 Increase / Decrease % ")
            print("5 Direct % (kitna percent nikalna hai)")

            choice = input("Enter choice: ")

    # ---------------- MARKS ----------------
            if choice == "1":
                total = int(input("Total marks: "))
                part = int(input("Obtained marks: "))
                percent = (part / total) * 100
                percent = round(percent, 2)

                print(f"📊 Tumne {percent}% score kiya")


    # ---------------- DISCOUNT ----------------
            elif choice == "2":
                total = int(input("Original price: "))
                paid = int(input("Paid price: "))
                discount = total - paid
                percent = (discount / total) * 100
                percent = round(percent, 2)

                print(f"💸 Tumhe {percent}% discount mila")

    # ---------------- PROFIT / Loss ----------------
            elif choice == "3":
                buy = int(input("Buy price: "))
                sell = int(input("Sell price: "))
                diff = sell - buy
                percent = (abs(diff) / buy) * 100
                percent = round(percent, 2)

                if diff > 0:
                    print(f"💰 Profit = {percent}%")
                elif diff < 0:
                    print(f"📉 Loss = {percent}%")
                else:
                    print("No profit no loss")

    
      # -------- GROWTH / CHANGE --------
            elif choice == "4":
                old = int(input("Old value: "))
                new = int(input("New value: "))

                diff = new - old
                percent = (abs(diff) / old) * 100
                percent = round(percent, 2)

                if diff > 0:
                    print(f"📈 Growth = {percent}%")
                elif diff < 0:
                    print(f"📉 Decrease = {percent}%")
                else:
                    print("No change")

    # -------- DIRECT --------
            elif choice == "5":
                value = int(input("Value: "))
                percent = int(input("Kitna % chahiye: "))

                result = (percent / 100) * value

                print(f"📊 {percent}% of {value} = {result}")

            else:
                print("Invalid")
    
       # avarage  new part      
 
        elif op == "12":
            print("\n📊 AVERAGE SYSTEM")
            print("1 Simple Average")
            print("2 Trading Average (multiple values)")

            choice = input("Enter choice: ")

    # -------- SIMPLE --------
            if choice == "1":
                n = int(input("Kitne numbers: "))
                total = 0

                for i in range(n):
                    num = int(input(f"Enter number {i+1}: "))
                    total += num

                avg = total / n
                avg = round(avg, 2)

                print(f"📊 Average = {avg}")

    # -------- TRADING --------
            elif choice == "2":
                n = int(input("Kitne din ka price: "))
                total = 0

                for i in range(n):
                    price = int(input(f"Day {i+1} price: "))
                    total += price

                avg = total / n
                avg = round(avg, 2)

                print(f"📈 Average Price = {avg}")
                print("👉 Ye market ka balance price hai")

            else:
                print("Invalid") 

        elif op == "13":
            print("\n📊 WEIGHTED AVERAGE SYSTEM")
            print("👉 Jis value ka importance zyada hai, uska weight zyada do\n")

            n = int(input("Kitne items (subjects / prices / data): "))

            total = 0
            total_weight = 0

            for i in range(n):
                value = int(input(f"Enter value {i+1}: "))
                weight = int(input(f"Enter weight {i+1}: "))

                total += value * weight
                total_weight += weight

            if total_weight == 0:
                print("❌ Weight zero nahi ho sakta")
                continue

            result = total / total_weight
            result = round(result, 2)

            print(f"\n📊 Weighted Average = {result}")

            print("\n🧠 Meaning:")
            print("👉 Jis value ka weight zyada tha, uska effect zyada pada")
            print("👉 Ye real average hai (simple average se zyada accurate 💀)")

            with open("history.txt", "a") as f:
                f.write(f"Weighted Average = {result}\n")            
        
# Gcd and lcm
        elif op == "14":
            print("\n📊 GCD / LCM SYSTEM")
            print("1. Sirf GCD")
            print("2. Sirf LCM")
            print("3. Dono")

            choice = input("Choose option: ")

            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            x, y = a, b

    # GCD
            while y != 0:
                x, y = y, x % y

                gcd = x
                lcm = (a * b) // gcd

                if choice == "1":
                    print(f"\nGCD = {gcd}")
                    print(f"👉 Matlab: dono numbers ko {gcd}-{gcd} me barabar baata ja sakta hai")

                elif choice == "2":
                    print(f"\nLCM = {lcm}")
                    print(f"👉 Matlab: {lcm} wo sabse chhota number hai jahan dono ek saath milte hain")

                elif choice == "3":
                    print(f"\nGCD = {gcd}")
                    print(f"👉 Matlab: equal grouping = {gcd}")

                    print(f"\nLCM = {lcm}")
                    print(f"👉 Matlab: meeting point = {lcm}")

                else:
                    print("Invalid choice")

                with open("history.txt", "a") as f:
                    f.write(f"GCD/LCM: {a},{b} -> GCD={gcd}, LCM={lcm}\n")    

      # prime number analyzer

        elif op == "15":              # 0 space
            import time              # 4 space

            num_input = input("Enter number: ").strip()   # 4 space

            if not num_input.isdigit():    # 4 space
                print("❌ Invalid input")  # 8 space
                continue                  # 8 space

            num = int(num_input)          # 4 space

            start_time = time.time()      # 4 space

            steps = []                    # 4 space
            factors = []                  # 4 space
            is_prime = False              # 4 space

            if num <= 1:                  # 4 space
                steps.append("Number 1 ya usse chhota hai")   # 8 space

            elif num == 2:                # 4 space
                is_prime = True           # 8 space
                steps.append("2 eklauta even prime hai")  # 8 space

            elif num % 2 == 0:            # 4 space
                factors.append(2)         # 8 space
                steps.append("Even number hai → 2 se divide hota hai")  # 8 sp
            else:                         # 4 space
                is_prime = True           # 8 space
                steps.append("Odd number → smart checking start")  # 8 space

                for i in range(3, int(num**0.5) + 1, 2):   # 8 space
                    steps.append(f"{num} % {i} check")     # 12 space

                    if num % i == 0:      # 12 space
                        is_prime = False # 16 space
                        factors.append(i)
                        steps.append(f"{i} se divide ho gaya")  # 16 space
                        break            # 16 space

            end_time = time.time()        # 4 space

            print("\n📊 RESULT:")        # 4 space

            if is_prime:                  # 4 space
                print("✅ Prime Number")  # 8 space
                print("👉 Reason: kisi bhi number se divide nahi hua")  # 8 space
            else:                         # 4 space
                print("❌ Not Prime")     # 8 space
                if factors:               # 8 space
                    print(f"👉 Factor mila: {factors[0]}")  # 12 space
                else:                     # 8 space
                    print("👉 Prime condition fail")  # 12 space

            print("\n🧠 Steps:")         # 4 space
            for s in steps[:10]:          # 4 space
                print("→", s)            # 8 space

            print(f"\n⏱ Time taken: {round(end_time - start_time, 6)} sec")  # 4 space

            if num > 1000000:             # 4 space
                print("\n⚠ Large Number Mode: calculation slow ho sakta hai")  # 8 space

            with open("history.txt", "a") as f:   # 4 space
                f.write(f"Prime Check: {num} → {'Prime' if is_prime else 'Not Prime'}\n")  # 8 space      
        
   #factors
   
        elif op == "16":              # 0 space
            num_input = input("Enter number: ").strip()   # 4 space

            if not num_input.isdigit():    # 4 space
                print("❌ Invalid input")  # 8 space
                continue                  # 8 space

            num = int(num_input)          # 4 space

            factors = []                  # 4 space
            pairs = []                    # 4 space

            for i in range(1,int(num**0.5) + 1):   # 4 space
                if num % i == 0:          # 8 space
                    factors.append(i)     # 12 space

                    if i != num // i:     # 12 space
                        factors.append(num // i)   # 16 space

                    pairs.append((i, num // i))   # 12 space

            factors.sort()                # 4 space

            print("\n📊 RESULT:")        # 4 space
            print(f"👉 Factors: {factors}")   # 4 space
            print(f"👉 Total factors: {len(factors)}")   # 4 space

            print("\n🔗 Factor Pairs:")  # 4 space
            for a, b in pairs:           # 4 space
                print(f"{a} × {b} = {num}")   # 8 space

            with open("history.txt", "a") as f:   # 4 space
                f.write(f"Factors: {num} → {factors}\n")   # 8 space        
   
        
def daily_life():
    print("\n🧠 DAILY LIFE SYSTEM")
    print("type exit to go back\n")
    # 🔗 LINKS (yaha apna link paste karo)
    links = {
        "bored": "LINK",
        "sad": "LINK",
        "focus": "LINK",
        "motivation": "LINK",
        "morning": "LINK",
        "night": "LINK",
        "tired": "LINK"
    }

    while True:
        user = input("\nAap kya chahte ho / feel kar rahe ho: ").lower()

        if user == "exit":
            print("Menu mai aa gaye")
            break

        # ================= SMART ROUTINE DETECTION =================

        elif any(word in user for word in ["student", "study", "padhai"]):
            print("\n🎓 STUDENT MODE 🔥")
            print("👉 Tension mat lo, system follow karo 💪")

            print("\n📌 Routine:")
            print("⏰ 5:30 AM - Utho")
            print("🧘 Meditation")
            print("📚 Hard subject study")
            print("🔁 Daily revision")
            print("🏃 Exercise")
            print("🌙 Proper sleep")

            print("\n💡 Tip:")
            print("👉 Consistency > Motivation")

            print("\n🎥 Video:", links["focus"])

        elif any(word in user for word in ["business", "work", "job"]):
            print("\n💼 BUSINESS MODE 🔥")
            print("👉 Smart kaam karo, hard nahi 😎")

            print("\n📌 Routine:")
            print("⏰ Early wake up")
            print("📊 Planning")
            print("📞 Work / Calls")
            print("📈 Growth work")
            print("💡 Learning daily")

            print("\n💡 Tip:")
            print("👉 Income = Skill × Consistency")

            print("\n🎥 Video:", links["motivation"])

        elif any(word in user for word in ["morning routine", "subah routine"]):
            print("\n🌅 MORNING ROUTINE")
            print("👉 Jaldi uthna")
            print("👉 Pani peena")
            print("👉 Exercise")
            print("👉 Meditation")
            print("👉 Planning")

            print("\n🎥 Video:", links["morning"])

        elif any(word in user for word in ["night routine", "raat routine"]):
            print("\n🌙 NIGHT ROUTINE")
            print("👉 Phone band karo")
            print("👉 Aaj ka review")
            print("👉 Kal ka plan")
            print("👉 Gratitude")
            print("👉 Jaldi so jao")

            print("\n🎥 Video:", links["night"])

        # ================= FEELING SYSTEM =================

        elif any(word in user for word in ["bore", "boring", "bored"]):
            print("\n😐 Bored ho?")
            print("👉 Mind ko refresh karo")

            print("\n⚡ Try this:")
            print("👉 Walk")
            print("👉 Music")
            print("👉 Kuch naya seekho")

            print("\n🔥 Secret:")
            print("👉 Boredom = growth ka signal")

            print("\n🎥 Video:", links["bored"])

        elif any(word in user for word in ["sad", "mood off", "dukhi", "depress"]):
            print("\n😔 Mood off hai?")
            print("👉 Ye temporary hai ❤️")

            print("\n🧠 Karo ye:")
            print("👉 Deep breathing")
            print("👉 Walk")
            print("👉 Kisi apne se baat karo")

            print("\n🔥 Yaad rakho:")
            print("👉 Tum strong ho 💪")

            print("\n🎥 Video:", links["sad"])

        elif any(word in user for word in ["focus", "concentrate"]):
            print("\n🎯 Focus Mode 🔥")

            print("\n📌 Steps:")
            print("👉 Phone door rakho")
            print("👉 25 min timer (Pomodoro)")
            print("👉 Ek kaam pe dhyan")
            print("👉 Break lo")

            print("\n💡 Tip:")
            print("👉 Distraction = enemy")

            print("\n🎥 Video:", links["focus"])

        elif any(word in user for word in ["motivation", "lazy", "alas"]):
            print("\n🔥 Motivation Mode")

            print("\n📌 Suno:")
            print("👉 Discipline = power")
            print("👉 Daily improve")
            print("👉 Hard work matters")

            print("\n💡 Reality:")
            print("👉 Motivation nahi, system chahiye")

            print("\n🎥 Video:", links["motivation"])

        elif any(word in user for word in ["morning", "subah"]):
            print("\n🌅 Morning Energy Tips")
            print("👉 Fresh start lo")
            print("👉 Body activate karo")

            print("\n🎥 Video:", links["morning"])

        elif any(word in user for word in ["night", "raat"]):
            print("\n🌙 Night Calm Mode")
            print("👉 Mind relax karo")
            print("👉 Screen time kam karo")

            print("\n🎥 Video:", links["night"])

        elif any(word in user for word in ["tired", "thak"]):
            print("\n😴 Recovery Mode")
            print("👉 Rest lo")
            print("👉 Water piyo")
            print("👉 Aankh band karo")

            print("\n🎥 Video:", links["tired"])

        # ================= HELP =================

        elif "help" in user:
            print("\n🆘 Commands:")
            print("👉 student / study")
            print("👉 business / work")
            print("👉 morning routine")
            print("👉 night routine")
            print("👉 bore / sad / focus / motivation")

        # ================= SMART FALLBACK =================

        else:
            print("\n🤖 Samajh nahi aaya")

            if "study" in user:
                print("👉 Shayad tum STUDENT mode chahte ho")
            elif "work" in user:
                print("👉 Shayad BUSINESS mode chahte ho")

            print("👉 Type 'help'")
    
    
def health_fitness():
    print("\n💪 HEALTH & FITNESS SYSTEM")
    print("type exit to go back\n")

    # 🔗 LINKS (yaha apna YouTube link paste karo)
    links = {
        "weight_loss": "LINK",
        "weight_gain": "LINK",
        "home_workout": "LINK",
        "gym": "LINK",
        "yoga": "LINK",
        "diet": "LINK"
    }

    while True:
        user = input("\nAap kya chahte ho (fitness): ").lower()

        if user == "exit":
            print("Menu mai aa gaye")
            break

        # ================= WEIGHT LOSS =================
        elif any(word in user for word in ["weight loss", "fat", "motapa", "lose weight", "ওজন কম"]):
            print("\n🔥 WEIGHT LOSS MODE")
            print("👉 Daily movement badhao")

            print("\n📌 Karo ye:")
            print("🏃 Running / Walk 30 min")
            print("🥗 Junk food band")
            print("💧 Pani zyada piyo")
            print("🍽 Light diet")

            print("\n💡 Tip:")
            print("👉 Fat slow jata hai, consistency rakho")

            print("\n🎥 Video:", links["weight_loss"])

        # ================= WEIGHT GAIN =================
        elif any(word in user for word in ["weight gain", "patla", "gain weight", "ওজন বাড়াও"]):
            print("\n💪 WEIGHT GAIN MODE")

            print("\n📌 Karo ye:")
            print("🍌 Banana daily")
            print("🥛 Milk + peanut")
            print("🍚 Zyada calories lo")
            print("🏋 Light workout")

            print("\n💡 Tip:")
            print("👉 Khana + rest = growth")

            print("\n🎥 Video:", links["weight_gain"])

        # ================= HOME WORKOUT =================
        elif any(word in user for word in ["home workout", "ghar", "no gym", "বাড়িতে"]):
            print("\n🏠 HOME WORKOUT")

            print("\n📌 Routine:")
            print("👉 Push-up 10x3")
            print("👉 Squat 15x3")
            print("👉 Plank 30 sec")
            print("👉 Jumping jack")

            print("\n💡 Tip:")
            print("👉 Daily 20-30 min enough")

            print("\n🎥 Video:", links["home_workout"])

        # ================= GYM =================
        elif any(word in user for word in ["gym", "muscle", "body", "জিম"]):
            print("\n🏋 GYM MODE")

            print("\n📌 Routine:")
            print("👉 Chest / Back / Legs split")
            print("👉 Protein diet")
            print("👉 Progressive overload")

            print("\n💡 Tip:")
            print("👉 Form > Weight")

            print("\n🎥 Video:", links["gym"])

        # ================= YOGA =================
        elif any(word in user for word in ["yoga", "meditation", "stress", "যোগ"]):
            print("\n🧘 YOGA MODE")

            print("\n📌 Karo ye:")
            print("👉 Pranayam")
            print("👉 Surya namaskar")
            print("👉 Deep breathing")

            print("\n💡 Benefit:")
            print("👉 Mind + body dono strong")

            print("\n🎥 Video:", links["yoga"])

        # ================= DIET =================
        elif any(word in user for word in ["diet", "khana", "food", "খাবার"]):
            print("\n🥗 DIET PLAN")

            print("\n📌 Basic:")
            print("👉 Protein (dal, egg)")
            print("👉 Fruits daily")
            print("👉 Junk kam")
            print("👉 Water high")

            print("\n💡 Tip:")
            print("👉 Diet = 70% result")

            print("\n🎥 Video:", links["diet"])

        # ================= BOY / GIRL =================
        elif any(word in user for word in ["boy", "ladka"]):
            print("\n👦 BOY FITNESS")
            print("👉 Muscle build + strength")
            print("👉 Gym / pushup / protein")

        elif any(word in user for word in ["girl", "ladki"]):
            print("\n👧 GIRL FITNESS")
            print("👉 Slim + fit body")
            print("👉 Yoga + light workout")
            print("👉 Diet clean rakho")

        # ================= HELP =================
        elif "help" in user:
            print("\n🆘 Try these:")
            print("👉 weight loss / gain")
            print("👉 home workout")
            print("👉 gym / yoga")
            print("👉 diet")
            print("👉 boy / girl")

        # ================= DEFAULT =================
        else:
            print("\n🤖 Samajh nahi aaya")
            print("👉 Type 'help'")   
    
def study_exam():
    print("\n📚 STUDY & EXAM SYSTEM")
    print("type exit to go back\n")

    # 🔗 LINKS (yaha apna YouTube link paste karo)
    links = {
        "focus": "LINK",
        "exam": "LINK",
        "revision": "LINK",
        "motivation": "LINK",
        "time_table": "LINK"
    }

    while True:
        user = input("\nAap kya chahte ho (study): ").lower()

        if user == "exit":
            print("Menu mai aa gaye")
            break

        # ================= FOCUS =================
        elif any(word in user for word in ["focus", "concentrate", "padhai", "পড়াশোনা"]):
            print("\n🎯 FOCUS MODE 🔥")
            print("👉 Distraction hatao")

            print("\n📌 Steps:")
            print("👉 Phone door rakho")
            print("👉 25 min timer (Pomodoro)")
            print("👉 Ek subject pe dhyan")
            print("👉 Break lo")

            print("\n💡 Tip:")
            print("👉 Deep work = success")

            print("\n🎥 Video:", links["focus"])

        # ================= EXAM =================
        elif any(word in user for word in ["exam", "paper", "test", "পরীক্ষা"]):
            print("\n📝 EXAM MODE 🔥")

            print("\n📌 Strategy:")
            print("👉 Important topics pe focus")
            print("👉 Previous year question solve")
            print("👉 Time management")

            print("\n💡 Rule:")
            print("👉 Smart study > Hard study")

            print("\n🎥 Video:", links["exam"])

        # ================= REVISION =================
        elif any(word in user for word in ["revision", "revise", "repeat", "রিভিশন"]):
            print("\n🔁 REVISION SYSTEM")

            print("\n📌 Karo ye:")
            print("👉 1 din baad revise")
            print("👉 3 din baad repeat")
            print("👉 7 din baad final revise")

            print("\n💡 Trick:")
            print("👉 Repeat = memory strong")

            print("\n🎥 Video:", links["revision"])

        # ================= TIME TABLE =================
        elif any(word in user for word in ["time table", "routine", "plan", "schedule"]):
            print("\n⏰ STUDY TIME TABLE")

            print("\n📌 Routine:")
            print("⏰ 5:30 - Wake up")
            print("📚 6–8 - Hard subject")
            print("🍽 Break")
            print("📖 10–1 - Study")
            print("😴 Rest")
            print("📘 4–6 - Revision")
            print("🧘 7 - Light study")
            print("🌙 10 - Sleep")

            print("\n💡 Tip:")
            print("👉 Fixed routine = success")

            print("\n🎥 Video:", links["time_table"])

        # ================= MOTIVATION =================
        elif any(word in user for word in ["motivation", "lazy", "alas", "অনুপ্রেরণা"]):
            print("\n🔥 STUDY MOTIVATION")

            print("\n📌 Suno:")
            print("👉 Aaj padhoge to kal jeetoge")
            print("👉 Time waste = life waste")
            print("👉 Discipline > Mood")

            print("\n💡 Reality:")
            print("👉 Topper banna hai to sacrifice karna padega")

            print("\n🎥 Video:", links["motivation"])

        # ================= SUBJECT HELP =================
        elif any(word in user for word in ["math", "science", "english", "subject"]):
            print("\n📖 SUBJECT STRATEGY")

            print("\n📌 Math:")
            print("👉 Practice daily")

            print("\n📌 Science:")
            print("👉 Concept samjho")

            print("\n📌 English:")
            print("👉 Reading + writing")

            print("\n💡 Tip:")
            print("👉 Weak subject pe zyada time do")

        # ================= HELP =================
        elif "help" in user:
            print("\n🆘 Try these:")
            print("👉 focus / padhai")
            print("👉 exam / test")
            print("👉 revision")
            print("👉 time table")
            print("👉 motivation")

        # ================= SMART FALLBACK =================
        else:
            print("\n🤖 Samajh nahi aaya")

            if "study" in user:
                print("👉 Shayad tum FOCUS chahte ho")
            elif "exam" in user:
                print("👉 Shayad tum EXAM help chahte ho")

            print("👉 Type 'help'")    
    
def online_earning():
    print("\n💰 ONLINE EARNING SYSTEM")
    print("type exit to go back\n")

    # 🔗 LINKS (yaha apne YouTube / channel links daalo)
    links = {
        "freelancing": "LINK",
        "youtube": "LINK",
        "affiliate": "LINK",
        "content": "LINK",
        "skill": "LINK",
        "mindset": "LINK"
    }

    while True:
        user = input("\nAap kya chahte ho (earning): ").lower()

        if user == "exit":
            print("Menu mai aa gaye")
            break

        # ================= BEGINNER PATH =================
        elif any(word in user for word in ["start", "beginner", "kaise kamaye", "earning start", "কিভাবে টাকা"]):
            print("\n🚀 BEGINNER PATH")
            print("👉 Pehle skill banao, fir earning ayegi")

            print("\n📌 Start karo:")
            print("👉 Mobile se basic skill sikho")
            print("👉 Free tools use karo")
            print("👉 Daily 2-3 ghanta kaam")

            print("\n💡 Reality:")
            print("👉 Jaldi paisa = scam")
            print("👉 Skill = real income")

            print("\n🎥 Video:", links["skill"])

        # ================= FREELANCING =================
        elif any(word in user for word in ["freelance", "client", "fiverr", "upwork"]):
            print("\n💻 FREELANCING MODE")

            print("\n📌 Kaam:")
            print("👉 Logo design")
            print("👉 Video editing")
            print("👉 Content writing")

            print("\n📌 Platform:")
            print("👉 Fiverr / Upwork")

            print("\n💡 Tip:")
            print("👉 Small start → big income")

            print("\n🎥 Video:", links["freelancing"])

        # ================= YOUTUBE =================
        elif any(word in user for word in ["youtube", "yt", "channel"]):
            print("\n🎬 YOUTUBE MODE 🔥")

            print("\n📌 Start karo:")
            print("👉 Niche choose karo")
            print("👉 Daily content upload")
            print("👉 Shorts + long video mix")

            print("\n💡 Income:")
            print("👉 Ad revenue")
            print("👉 Sponsorship")
            print("👉 Affiliate")

            print("\n🎥 Video:", links["youtube"])

        # ================= AFFILIATE =================
        elif any(word in user for word in ["affiliate", "product", "sell", "commission"]):
            print("\n🛒 AFFILIATE MODE")

            print("\n📌 Kaam:")
            print("👉 Product promote karo")
            print("👉 Link share karo")
            print("👉 Sale pe commission")

            print("\n💡 Tip:")
            print("👉 Trust build karo")

            print("\n🎥 Video:", links["affiliate"])

        # ================= CONTENT CREATION =================
        elif any(word in user for word in ["content", "reel", "shorts", "instagram"]):
            print("\n📱 CONTENT CREATOR MODE")

            print("\n📌 Kaam:")
            print("👉 Reels / Shorts banao")
            print("👉 Daily upload")
            print("👉 Trending topic pakdo")

            print("\n💡 Income:")
            print("👉 Brand deal")
            print("👉 Followers → money")

            print("\n🎥 Video:", links["content"])

        # ================= SKILL BASED =================
        elif any(word in user for word in ["skill", "coding", "editing", "design"]):
            print("\n🧠 SKILL MODE 🔥")

            print("\n📌 Learn karo:")
            print("👉 Coding")
            print("👉 Video editing")
            print("👉 Graphic design")

            print("\n💡 Rule:")
            print("👉 High skill = high income")

            print("\n🎥 Video:", links["skill"])

        # ================= MINDSET =================
        elif any(word in user for word in ["mindset", "soch", "lazy", "fail"]):
            print("\n🧠 MONEY MINDSET")

            print("\n📌 Yaad rakho:")
            print("👉 Skill pe focus karo")
            print("👉 Daily kaam karo")
            print("👉 Consistency hi power hai")

            print("\n💡 Truth:")
            print("👉 6 mahine me result aayega")

            print("\n🎥 Video:", links["mindset"])

        # ================= HELP =================
        elif "help" in user:
            print("\n🆘 Try these:")
            print("👉 start earning")
            print("👉 freelancing")
            print("👉 youtube")
            print("👉 affiliate")
            print("👉 content")
            print("👉 skill")

        # ================= SMART FALLBACK =================
        else:
            print("\n🤖 Samajh nahi aaya")

            if "earn" in user:
                print("👉 Shayad tum earning start karna chahte ho")
            elif "video" in user:
                print("👉 Shayad tum YouTube karna chahte ho")

            print("👉 Type 'help'")    
    
def youtube_growth():
    print("\n🎬 YOUTUBE GROWTH SYSTEM")
    print("type exit to go back\n")

    # 🔗 LINKS (apne videos daalo)
    links = {
        "start": "LINK",
        "shorts": "LINK",
        "viral": "LINK",
        "editing": "LINK",
        "title": "LINK",
        "growth": "LINK"
    }

    while True:
        user = input("\nAap kya chahte ho (YouTube): ").lower()

        if user == "exit":
            print("Menu mai aa gaye")
            break

        # ================= START =================
        elif any(word in user for word in ["start", "channel", "begin"]):
            print("\n🚀 START YOUTUBE")

            print("\n📌 Steps:")
            print("👉 Ek niche choose karo")
            print("👉 Daily upload karo")
            print("👉 Overthinking mat karo")

            print("\n💡 Rule:")
            print("👉 Start fast, improve later")

            print("\n🎥 Video:", links["start"])

        # ================= SHORTS =================
        elif any(word in user for word in ["shorts", "reel", "viral short"]):
            print("\n🔥 SHORTS STRATEGY")

            print("\n📌 Karo ye:")
            print("👉 10–20 sec video")
            print("👉 First 2 sec hook strong")
            print("👉 Fast editing")

            print("\n💡 Secret:")
            print("👉 Shorts = fastest growth")

            print("\n🎥 Video:", links["shorts"])

        # ================= VIRAL =================
        elif any(word in user for word in ["viral", "views", "reach"]):
            print("\n💀 VIRAL SYSTEM")

            print("\n📌 Formula:")
            print("👉 Hook + Emotion + Curiosity")
            print("👉 Trending topic use karo")
            print("👉 Repeat winning content")

            print("\n💡 Truth:")
            print("👉 Viral luck nahi, system hai")

            print("\n🎥 Video:", links["viral"])

        # ================= EDITING =================
        elif any(word in user for word in ["edit", "editing", "video edit"]):
            print("\n✂️ EDITING SYSTEM")

            print("\n📌 Karo ye:")
            print("👉 Fast cuts")
            print("👉 Text add karo")
            print("👉 Sound effect use karo")

            print("\n💡 Tip:")
            print("👉 Editing = retention")

            print("\n🎥 Video:", links["editing"])

        # ================= TITLE =================
        elif any(word in user for word in ["title", "thumbnail", "click"]):
            print("\n🧲 TITLE + THUMBNAIL")

            print("\n📌 Karo ye:")
            print("👉 Curiosity create karo")
            print("👉 Numbers use karo")
            print("👉 Simple rakho")

            print("\n💡 Rule:")
            print("👉 Click = growth")

            print("\n🎥 Video:", links["title"])

        # ================= GROWTH =================
        elif any(word in user for word in ["grow", "subscriber", "increase"]):
            print("\n📈 GROWTH SYSTEM 🔥")

            print("\n📌 Formula:")
            print("👉 Consistency")
            print("👉 Quality")
            print("👉 Patience")

            print("\n💡 Reality:")
            print("👉 100 video = real growth start")

            print("\n🎥 Video:", links["growth"])

        # ================= HELP =================
        elif "help" in user:
            print("\n🆘 Try these:")
            print("👉 start youtube")
            print("👉 shorts")
            print("👉 viral")
            print("👉 editing")
            print("👉 title")
            print("👉 growth")

        # ================= SMART FALLBACK =================
        else:
            print("\n🤖 Samajh nahi aaya")

            if "video" in user:
                print("👉 Shayad tum editing ya shorts chahte ho")
            elif "money" in user:
                print("👉 Shayad tum growth chahte ho")

            print("👉 Type 'help'")    
    
def editing_system():
    print("\n✂️ EDITING SYSTEM (PRO)")
    print("type exit to go back\n")

    # 🔗 LINKS (yaha apne YouTube tutorial daalo)
    links = {
        "basic": "LINK",
        "shorts": "LINK",
        "advanced": "LINK",
        "text": "LINK",
        "sound": "LINK",
        "color": "LINK"
    }

    while True:
        user = input("\nAap kya chahte ho (editing): ").lower()

        if user == "exit":
            print("Menu mai aa gaye")
            break

        # ================= BASIC =================
        elif any(word in user for word in ["basic", "start", "begin"]):
            print("\n🎬 BASIC EDITING")

            print("\n📌 Start karo:")
            print("👉 VN / CapCut use karo")
            print("👉 Cut + trim sikho")
            print("👉 Simple text add karo")

            print("\n💡 Tip:")
            print("👉 Clean video > heavy effect")

            print("\n🎥 Video:", links["basic"])

        # ================= SHORTS =================
        elif any(word in user for word in ["shorts", "reel", "instagram"]):
            print("\n🔥 SHORTS EDITING")

            print("\n📌 Karo ye:")
            print("👉 Fast cuts (1–2 sec)")
            print("👉 Zoom in/out")
            print("👉 Subtitle add karo")

            print("\n💡 Secret:")
            print("👉 First 3 sec = hook 💀")

            print("\n🎥 Video:", links["shorts"])

        # ================= ADVANCED =================
        elif any(word in user for word in ["advanced", "pro", "cinematic"]):
            print("\n🎥 ADVANCED EDITING")

            print("\n📌 Karo ye:")
            print("👉 Transition use karo")
            print("👉 Slow motion")
            print("👉 Motion effect")

            print("\n💡 Tip:")
            print("👉 Over edit mat karo")

            print("\n🎥 Video:", links["advanced"])

        # ================= TEXT =================
        elif any(word in user for word in ["text", "subtitle", "caption"]):
            print("\n📝 TEXT SYSTEM")

            print("\n📌 Karo ye:")
            print("👉 Bold text use karo")
            print("👉 2–3 word per line")
            print("👉 Highlight keywords")

            print("\n💡 Rule:")
            print("👉 Text = attention पकड़ता है")

            print("\n🎥 Video:", links["text"])

        # ================= SOUND =================
        elif any(word in user for word in ["sound", "music", "audio"]):
            print("\n🔊 SOUND SYSTEM")

            print("\n📌 Karo ye:")
            print("👉 Background music")
            print("👉 Beat match cut")
            print("👉 Sound effect add")

            print("\n💡 Secret:")
            print("👉 Sound = emotion control")

            print("\n🎥 Video:", links["sound"])

        # ================= COLOR =================
        elif any(word in user for word in ["color", "filter", "look"]):
            print("\n🎨 COLOR GRADING")

            print("\n📌 Karo ye:")
            print("👉 Brightness adjust")
            print("👉 Contrast")
            print("👉 Warm tone")

            print("\n💡 Tip:")
            print("👉 Natural look best")

            print("\n🎥 Video:", links["color"])

        # ================= HELP =================
        elif "help" in user:
            print("\n🆘 Try these:")
            print("👉 basic editing")
            print("👉 shorts editing")
            print("👉 advanced")
            print("👉 text")
            print("👉 sound")
            print("👉 color")

        # ================= SMART FALLBACK =================
        else:
            print("\n🤖 Samajh nahi aaya")

            if "video" in user:
                print("👉 Shayad tum editing start karna chahte ho")
            elif "viral" in user:
                print("👉 Shayad tum shorts editing chahte ho")

            print("👉 Type 'help'")   
   
    #main menu list
while True:
    print("1 choice chat ")
    print("2 choice calculator")
    print("3 choice history calculetor file")
    
    print("4 choice daily life tips")
    print("5 choice Health & Fitness tips")
    print("6 choice study & Exam tips")
    print("7 choice Online Earning tips")
    print("8 choice youtube grow tips")
    print("9 choice Editing tips")
    print("10 choice exit")
    
    choice = input("Enter your choice:").lower()
    
        
    
    if choice == "1":
        chat()    
    
    elif choice == "2":
        calculator()
    
    elif choice == "3":
        try:
            with open("history.txt", "r") as f:
                lines = f.readlines()
                
                if not lines:
                    print("no history found")
                    
                else:
                    print(f"Total history: {len(lines)}\n")
                
                for line in lines[-10:]:
                    print(line.strip())
                    
        except:
            print("no history found")
            
    elif choice == "4":
        daily_life()
    
    elif choice == "5":
        health_fitness()    
        
    elif choice == "6":
        study_exam()
    
    elif choice == "7":
        online_earning()
    
    elif choice == "8":
        youtube_growth()
    
    elif choice == "9":
        editing_system()
    else:
        print("Invalid choice, try again ✔")
                
