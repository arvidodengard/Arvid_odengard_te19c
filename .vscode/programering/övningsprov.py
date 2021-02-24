'''
# Uppgift 3
def f(x):
    return x / 3

x = 1 + 3 + 5

print(f(x))

# Uppgift 4


def f(r):
    return (4*3.14*r**3) / 3


r = float(input("radiens värde är:"))

print(f(r))


# Uppgift 5
mening = input("Din mening är:  ")

mening = mening.split()
print(f"meningen innehåller {len(mening)} ord")

# Uppgift 6
import random as rnd 

första = rnd.randint(1,10)
andra = rnd.randint(1,10)

def gångertabell(x):
    x = första*andra
    return x

svar = int(input(f"vad är {första} gånger {andra}?"))

if svar == gångertabell(x):
    print("korrekt")

else:
    print("fel")

# Uppgift 7
import random as rnd 
femmor = 0 
for i in range(10000):
  tärningskast = rnd.randint(1,6) 
    if tärningskast == 5:
      femmor = femmor +1
print(femmor) 

# Uppgitft 8
tal = int(input("antal pengar:"))
tusenlappar = 0
while tal > 999.99999:
    tusenlappar = tusenlappar + 1
    tal = tal - 999.99999

tvåhundralappar = 0
while tal > 199.99999:
    tvåhundralappar = tvåhundralappar + 1
    tal = tal - 199.99999

hundralappar = 0
while tal > 99.99999:
    hundralappar = hundralappar + 1
    tal = tal - 99.99999

femtiolappar = 0
while tal > 49.9999999:
    femtiolappar = femtiolappar + 1
    tal = tal - 49.9999999

femma = 0
while tal > 4.9999999:
    femma = femma + 1
    tal = tal - 4.9999999

enkrona = 0
while tal > 0.9999999:
    enkrona = enkrona + 1
    tal = tal - 0.9999999

print(tusenlappar, tvåhundralappar, hundralappar, femtiolappar, femma, enkrona)

# Uppgift 10
import kortlek


def skrivUtHand(hand):
    print("Dina kort är: ", end="")
    for kort in hand:
        print(str(kort) + ", ", end="")


def räknaPoäng(hand):
    poäng = 0
    for kort in hand:
        if kort == "J" or kort == "Q" or kort == "K":
            poäng += 10
        elif kort == "A" and poäng < 11:
            poäng += 11
        elif kort == "A" and poäng >= 11:
            poäng += 1
        else:
            poäng += kort
    return poäng


def checkaVinnare(hand, dealer):
    dealerPoäng = räknaPoäng(dealer)
    spelare1Poäng = räknaPoäng(hand)

    print(f"Dealerns kort är {dealer[0]} och {dealer[1]}")
    print(f"Dealerns totala poäng: {dealerPoäng}")
    print(f"Spelare1 totala poäng: {spelare1Poäng}")

    if spelare1Poäng == 21:
        print("Blackjack, du vinner")
    elif spelare1Poäng <= dealerPoäng or spelare1Poäng > 21:
        print("Dealern tar dina pengar")
    else:
        print("Du vinner")


# spel-loop
def spel_loop():
    while True:
        spela = input(
            "Vill du spela? (j för ja, valfri tangent för att avsluta)")

        if spela != "j":
            break
        lek = kortlek.skapaKortlek()
        # dealer tar två kort
        dealer = [lek.pop(0), lek.pop(0)]

        print(f"Dealerns första kort är {dealer[0]}")

        hand = [lek.pop(0), lek.pop(0)]

        print(f"Dina första två kort är {hand[0]} och {hand[1]}")

        fortsätt = True

        # omgång
        while fortsätt:
            # fråga om användaren vill ta ett till kort
            taKort = input("Ta nytt kort? (j för ja, annan tangent för nej)")

            if taKort == "j" and räknaPoäng(hand) <= 21:
                # dela ut kort
                hand.append(lek.pop(0))
                skrivUtHand(hand)
            else:
                fortsätt = False  # avsluta spelet

        checkaVinnare(hand, dealer)


if __name__ == "__main__":
    spel_loop()

'''


