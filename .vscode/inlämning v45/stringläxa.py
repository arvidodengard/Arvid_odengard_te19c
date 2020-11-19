#Uppgift 1
namn = "Arvid"
print(f"Ditt namn innehåller {len(namn)} bokstäver")

#Uppgift 2
mening = "En bild säger mer än tusen ord, en matematisk formel säger mer än tusen bilder"

mening = mening.split()
print(f"meningen innehåller {len(mening)} ord")

#Uppgift 3a

ord = (input("din mening: "))

if ord == ord[::-1]:
    print("är ett palindrom")

else:
    print("ej ett palindrom")

#Uppgift 3b
ord = input("Mata in en mening av tecken med mellanslag och skiljetecken")
ord = ord.replace (" ", "")
ord = ord.replace (",", "")
ord = ord.replace (".", "")

if ord[::-1] == ord:
    print("Är ett palindrom")
else:
    print("Är ej ett palindrom")




