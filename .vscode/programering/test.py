
def f(x):
    return 2*x + 2*y

x = 4
y = 6

print(f(x))

# 

import random as rnd

första = rnd.randint(1,10)
andra = rnd.randint(1,10)

def gångertabell(x):
    return x

x = första*andra

svar = float(input(f"vad är {första} x {andra}="))

if svar == gångertabell(x):
    print("korrekt")

elif svar != gångertabell(x):
    print("fel")

#

import random as rnd

tal = rnd.randint(0,101)
g = 0
while g != tal:
    g = float(input("gissning="))
    if tal != g:
     print("fel")
    elif tal == g:
        print("rätt svar")


# 
summa = int(input("summa"))
kostnad = int(input("kostnad"))
betala = summa- kostnad

def växla(betala):
    kontanter = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    sedlar = ["tusenlappar", "femhundra", "tvåhundra", "hundra", "femtio", "tjugo", "tio", "fem", "enkronor"]

    for i in range(len(kontanter)):
        antal = betala//kontanter[i]
        betala %= kontanter[i]
        print(f"{antal} {sedlar[i]}", end=", ")
växla(betala)

# 
f = str(input("din mening"))

for i in range(len(f)):
    lista = [["a",1],["b",2],["c",3]]
    if f == lista[i][0]:
        print(lista[i][1])
        
frukter = ["kiwi", "äpplen", "bananer", "jordgubbar"]

Godfrukt = frukter[3]
print(Godfrukt[3])

tal = [i**2 for i in range(5)]
print(tal)