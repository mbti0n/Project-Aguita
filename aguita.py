import time, os, random
string0 = """  │ │
 ╱   ╲
│     │
│     │
│     │
│     │
│     │
│     │
└─────┘
"""

string25 = """  │ │
 ╱   ╲
│     │
│     │
│     │
│     │
│~~~~~│
│~~~~~│
└─────┘
"""

string50 = """  │ │
 ╱   ╲
│     │
│     │
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
└─────┘
"""

string75 = """  │ │
 ╱   ╲
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
└─────┘
"""

string100 = """  │~│
 ╱~~~╲
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
│~~~~~│
└─────┘
"""

drop1 = """   ║
   ║
   │
   │"""
   
drop2 = """   │
   │
   ║
   ║"""
   
drop3 = """   
   
   
   """

dropSelect = [drop1, drop2]
isStopped = False
counter = 0
bottleSaved = 0

while not isStopped:
    current = random.randint(0, 100)
    water = ""
    if current < 25:
        water = string0
    elif current >= 25 or current < 50:
        water = string25
    elif current >= 50 or current < 75:
        water = string50
    elif current >= 75 or current < 100:
        water = string75
    elif current >= 100:
        water = string100

    os.system('cls' if os.name == 'nt' else 'clear')
    print(water)
    time.sleep(2)

    while current <= 100:
        os.system('cls' if os.name == 'nt' else 'clear')
        if counter == 100:
            counter = 0
            bottleSaved += 1
        print(f"Bottle saved: {bottleSaved}")
        print("━━━━━━━━")
        print(random.choice(dropSelect))
        print(water)
        if current < 25:
            water = string0
        elif current >= 25 and current < 50:
            water = string25
        elif current >= 50 and current < 75:
            water = string50
        elif current >= 75 and current < 100:
            water = string75
        elif current >= 100:
            water = string100
        
        current += 1
        counter += 1
        time.sleep(0.15)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("━━━━━━━━")
    print(drop3)
    print(water)

    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(water)
    print("Done!")

    continueInput = input("Continue? y/n   ")
    if continueInput == "n":
        isStopped = True
        
print(f"Bottle saved: {bottleSaved}")
