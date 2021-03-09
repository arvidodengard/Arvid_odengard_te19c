# Uppgift 1 a,b,c
import random as rnd 
rolls = []
femmor = 0

with open ("diceRoll.txt", "w") as f1: 
    for i in range(10):
        roll = rnd.randint (1, 6)
        rolls.append(roll)
        
        if roll == 5:
            femmor += 1


        sortedroll = sorted(rolls)

        f1.write(f"{roll}")
    f1.write(f"\n {sortedroll} \n{femmor}")

# uppgift 2 a, b, c
with open ("Provresultat.txt", "r") as f2:
    for rad in f2:
        print(rad)
    
    for line in sorted(open('Provresultat.txt')):
      print(line, end='')

with open("Provresultat.txt", "r+") as f2:
    lines = f2.readlines()
    lines.sort()
    f2.write(f" {lines}")

with open("Provresultat.txt", "r+") as f3:
    for i in f3: 
        resultat = int(i[-3:-1])
        if resultat < 20:
            betyg ="F"
        elif resultat > 20 and resultat <29:
            betyg = "E"
        elif resultat > 29 and resultat <39:
            betyg = "D"
        elif resultat > 39 and resultat <49:
            betyg = "C"
        elif resultat > 40 and resultat <59:
            betyg = "B"
        elif resultat > 50:
            betyg = "A"
        f3.write(f" \n {betyg}")


# Uppgift 3

import matplotlib.pyplot as plt

bokstav = [] # gör två tomma listor 
procent = []

with open("NPvt19Ma2A.txt", "r") as f4:
    for i in f4:
        
        bokstav[i] = i[0] # ger att bokstav rad 1 är = första tecknet i rad 1
        temp = i[2:] # ger alla tecknen förutom de två första på raden.
        procent[i] = temp[:-1] # ger raden över + inte den sista i raden.
    plt.pie.subplot(procent2, labels = bokstav2) # ger cirkeldiagramet värdena från över / borde bara haft en plot men har två
    # eftersom jag inte fick subplot att fungera.
    plt.show()

bokstav2 = [] # gör två tomma listor till 
procent2 = []
with open("NPvt19Ma2C.txt", "r") as f5:
    for i in f5:
        
        bokstav2[i] = i[0]
        temp2 = i[2:]
        procent2[i] = temp2[:-1]
    plt.pie.subplot(procent2, labels = bokstav2)
    plt.show()



      