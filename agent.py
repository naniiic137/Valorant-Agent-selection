#you need to install pyautogui 
#just use cmd and type pip install pyautogui

from pyautogui import click, PAUSE

PAUSE = 0.01


agents = dict()

x = [539, 633, 716, 797, 878, 972, 1044, 1141, 1214, 1295, 1376]
y = [538, 622, 711, 790, 876, 960, 1053, 1131, 1218, 1291, 1375]
s = x + y

for i in range(len(s)):
    agents[i + 1] = s[i]


agent = [
    "Astra",
    "Breach",
    "Brimstone",
    "Chamber",
    "Cypher",
    "Deadlock",
    "Fade",
    "Gekko",
    "Harbor",
    "jett",
    "KAYO",
    "KilljoY",
    "Neon",
    "Omen",
    "Phoenix",
    "Raze",
    "Reyna",
    "Sage",
    "Skye",
    "Sova",
    "Viper",
    "yuro",
]

j = 0
for c in agent:
    j += 1
    print(j, "-", c)

print("\n")
lock = int(input("what agent number you want to lock : "))

i = 0
while i < 100:
    i += 1
    if lock < 11:
        click(agents[lock], 923)
    else:
        click(agents[lock], 1000)
    click(953, 812)


input("i hope you get it ;) ")
