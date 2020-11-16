förnamn = "arvid"
efternamn = "odengård"

namn = förnamn + "\t" + efternamn
ålder = 17
adress = "yeet 9"
telefon = 112

personuppgift = "namn " + namn + "\n" + "ålder " + ålder + "\n" + "telefon " + str(telefon)



# indexering

alfabet = "abcdefghijklmnopqrstuvwzåäö"
print(f"Alfabetet innehåller {len(alfabet)} bokstäver")

print(f"bokstav på index 0: {alfabet[5]}")

#split funktion
favoiritämnen = "matematik programmering teknok webbutveckling fysik"

favoritämnen = favoritämnen.split()
print(favoritämnen)

for ämne in favoritämnen:
    print(f"ämne {ämne}")