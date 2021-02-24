import random as rnd 

första = rnd.randint(1,10)
andra = rnd.randint(1,10)

def gångertabell(x):
    return x

x = första*andra

svar = float(input(f"vad är {första} x {andra}="))

if svar == gångertabell(x):
    print("rätt svar")

elif svar != gångertabell(x):
    print("fel")


# 
import random as rnd

tal = rnd.randint(0,101)
g = 0

while g != tal:
    g = float(input("Gissning="))
    if g != tal:
        print("fel")
    elif g == tal:
        print("korrekt")
