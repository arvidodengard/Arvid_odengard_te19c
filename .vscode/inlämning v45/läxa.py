# uppgift a

x = 0.5 # Ger bokstaven x ett värde.
y = 0.5 # Ger bokstaven y ett värde.
c = x**2+y**2 # Kodar en formel för x^2 + y^2 och ger den värdet c.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.

# uppgift b 

x = 1 # Ger bokstaven x ett värde.
y = 1 # Ger bokstaven y ett värde.
c = x**2+y**2 # Kodar en formel för x^2 + y^2 och ger den värdet c.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.

# uppgift c

x = 0.5 # Ger bokstaven x ett värde.
y = 0.5 # Ger bokstaven y ett värde.
c = x**2+y**2 # Kodar en formel för x^2 + y^2 och ger den värdet c.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.


# uppgift d

import random as rnd  # Importar random som rnd altså ger random värded rnd.
import matplotlib.pyplot as plt # importar matplotlib.pyplot som plt, ger värde.
for x in range (50): # Upprepar x 50 gånger
    x = rnd.uniform(-1,1)
    y = rnd.uniform(-1,1)

    plt.plot (x,y)
plt.grid()
plt.show() # visar grafen

# uppgift e
import random as rnd 
for x in range (100):
    x = rnd.uniform(-1,1)
    y = rnd.uniform(-1,1)
    if x**2+y**2 <=1: print (x)

# hade 26 punkter utanför och 24 innanför altså 24/50 = 0.48

# uppgift f

i = 0.48 *4 # Ger i värdet av två tal som gångras med varandra 
print (i) # skriver ut svaret på i

# fick efter 1.92 eftersom den håller samma mönster
# så att gångra svaret med 4 är = att gångra antal kast

# uppgift g
import random as rnd 
import matplotlib.pyplot as plt 
for x in range (100):
    x = rnd.uniform(-1,1)
    y = rnd.uniform(-1,1)
    if x**2+y**2 <=1:
      plt.plot (x,y, '*r')
    else: 
      plt.plot (x,y, '*b')
plt.grid()
plt.show()

# ju större radie = mer kast utanför, fler kast följer samma mönster 
# med hur många pillar som hamnar innanför och utanför.

# uppgift 2 (a)

for i in range(1,101): #Upprepar i 100 gånger
    print(i, end =" ")

# uppgift b

for i in range(1,101): #Upprepar i 100 gånger
   
    if i%5 == 0:
        print("burr")
    else:    
        print(i, end =" ")

# Upgifft c

g = float(input("tal")) 
for i in range(1,101):
    
    if i%g == 0:
        print("burr")
    else:    
        print(i, end =" ")

# Uppgift d

g = float(input("talet burr")) 
f = float(input("talet birr"))
for i in range(1,101):
    
    if i%g == 0:
        print("burr")

    elif i%f == 0:
        print ("birr")

    else:    
        print(i, end =" ")

# Uppgift e

g = float(input("talet burr")) # Implementar g som burr altså vilken multiple burr ska vara.
f = float(input("talet birr")) # Implementar f som birr altså vilken multiple birr ska vara.
y = int(input("start")) # Ger startvärded bokstaven y.
r = int(input("slut")) # Ger slutvärded bokstaven r

for i in range(y,r):
    
  if i%g == 0:
    print("burr")

  elif i%f == 0:
    print ("birr")

    if i%g == 0 and i%f == 0:

  else:    
    print(i, end =" ")

# Som förbättring så skulle man kunna ha med mer tal exempel negativa tal, decimaltal eller upphöjt.
# eftersom det gör koden mer flexibel.
# men jag kommer att fokusera på decimaltal.
# 

