# Uppgift 1
n = 1
summa = 0 
while n < 101:
     summa = summa + n   
     n += 1
print (f"1+3+5... = {summa}")
    


# Uppgift 2
n = 1
summa = 0 
while n < 101:
     summa = summa + n   
     n += 2
     
print (f"1+3+5... = {summa}")

# Uppgift 5 

import random

tal = random.randint(1,101)
g = -1
while g != tal:
    g = float(input("gissning"))
    if tal < g:
     print("talet är mindre")
    elif tal > g:
      print("talet är större")
    elif tal == g:
     print("rätt svar")



