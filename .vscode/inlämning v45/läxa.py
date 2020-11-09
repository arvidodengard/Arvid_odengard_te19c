# uppgift a

x = 0.5 # Ger bokstaven x ett värde.
y = 0.5 # Ger bokstaven y ett värde.
c = x**2+y**2 # Ger variabeln c värdet x^2 + y^2.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.

# uppgift b 

x = 1 # Ger bokstaven x ett värde.
y = 1 # Ger bokstaven y ett värde.
c = x**2+y**2 # Ger variabeln c värdet x^2 + y^2.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.

# uppgift c

x = 0.5 # Ger bokstaven x ett värde.
y = 0.5 # Ger bokstaven y ett värde.
c = x**2+y**2 # Ger variabeln c värdet x^2 + y^2.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.


# uppgift d

import random as rnd  # Importar random som rnd altså ger random aliaset rng.
import matplotlib.pyplot as plt # importar matplotlib.pyplot som plt, ger värde.
for n in range (50): # Upprepar x 50 gånger.
    x = rnd.uniform(-1,1) #Tildlelar x ett slumptal mellan -1 och 1.
    y = rnd.uniform(-1,1) #Tildlelar y ett slumptal mellan -1 och 1.
    print(x,y) # Skriver ut värdet på x och y.


# uppgift e
inne = 0 # Inne är en variabel för alla pilar som landar inne i cirkeln.
f = 0 # är en variabel som indikerar om pilen är innanför eller utanför.
import random as rnd # ger "random" namnet rnd
for n in range (100): # Upprepar n 100 gånger altså upprepar allt innom ranged 100 gånger
    x = rnd.uniform(-1,1) # Tildlelar x ett slumptal mellan -1 och 1.
    y = rnd.uniform(-1,1) # Tildlelar y ett slumptal mellan -1 och 1.
    f = x**2+y**2 # Tilldelar variablen f värdet x^2 + y^2
    if f <=1: # Om f (x^2+y^2) är mindre eller = med 1 så skall (inne) adera 1 pil (om pilen är i cirkeln så adderas 1)
      inne = inne +1 # hör ihop med raden över men om påståendet stämmer så adderas 1 på vad inne var före (börjar från 0 och slutar vid 100)

print(inne/n) # Skriver ut vad inne blev / antalet ex pilar kastade

# uppgift f
# Svarat från e gånger 4 narmar sig (pi) statistiskt sett.
# eftersom det är cirkels area.


# uppgift g
import random as rnd # ger "random" namnet rnd
import matplotlib.pyplot as plt # ger "matplotlib.pyplot" namnet plt
for n in range (100): # Upprepar n 100 gånger altså upprepar allt innom ranged 100 gånger
    x = rnd.uniform(-1,1) # Tildlelar x ett slumptal mellan -1 och 1.
    y = rnd.uniform(-1,1) # Tildlelar y ett slumptal mellan -1 och 1.
    if x**2+y**2 <=1: # kollar för alla värden på x,y om det är <= 1 eller inte.
      plt.plot (x,y, '*r') # ger alla tal <= 1 (alla pilar inne i cirkeln) färjen röd i diagramet.
    else: 
      plt.plot (x,y, '*b') # ger alla tal över 1 (alla pilar utanför cirkeln) färjen blå i diagramet.
plt.grid() # målar ut linjer i ett diagram.
plt.show() # visar diagramet.

# uppgift h
# ju mindre radie = mer % av kasten hamnar utanför och (1) är den största radien.


# uppgift 2 (a)

for i in range(1,101): #Upprepar i 100 gånger eller då all kod 100 gånger
    print(i, end =" ") # Print skriver ut i och end ändrar hur det skrivs ut istället för allt vertikalt så skrivs koden horisontellt.

# uppgift b

for i in range(1,101): #Upprepar i 100 gånger.
   
    if i%5 == 0: # Om 5 gångras med något och det blir 0 över så stämmer påståended ex 11 då blir det 10 och 1 över altså stämmer det bara när inget blir över.
        print("burr") # skriver ut burr om påståendet stämmer.
    else:    
        print(i, end =" ") # skriver ut i och skriver svaret horisontellt.

# Upgifft c

g = float(input("tal")) # Gör en input (valfritt tal).
for i in range(1,101): # Upprepar i (koden) fån 1 - 101 .
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut
    else:    
        print(i, end =" ") # skriver ut i och svaret är horisontellt

# Uppgift d

g = float(input("talet burr")) # Gör en input (valfritt tal).
f = float(input("talet birr")) # Gör en input (valfritt tal).
for i in range(1,101): # Upprepar i (koden) fån 1 - 101 .
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut.

    if i%f == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print ("birr") # Om påståendet stämmer så skrivs birr ut.
        
    else:    
        print(i, end =" ") # Skriver ut i horisontellt.

# Uppgift e

g = float(input("talet burr")) # Implementar g som burr altså vilken multiple burr ska vara.
f = float(input("talet birr")) # Implementar f som birr altså vilken multiple birr ska vara.
y = int(input("start")) # Ger startvärded bokstaven y.
r = int(input("slut")) # Ger slutvärded bokstaven r

for i in range(y,r): # Upprepar i (koden) för (y-r gånger)
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut

    if i%f == 0:  # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print ("birr") # Om talet stämmer så skrivs birr ut
        
    else:    
        print(i, end =" ") # printar i horisontellt

# Som förbättring så skulle man kunna ha med mer tal exempel negativa tal, decimaltal eller upphöjt.
# eftersom det gör koden mer flexibel.
# men jag kommer att fokusera på att även göra ett diagram så det ser tydligt ut.

# Under så är ett misslyckat försök av att få ett fungerande diagram
import matplotlib.pyplot as plt
g = float(input("talet burr")) # Implementar g som burr altså vilken multiple burr ska vara.
f = float(input("talet birr")) # Implementar f som birr altså vilken multiple birr ska vara.
y = int(input("start")) # Ger startvärded bokstaven y.
r = int(input("slut")) # Ger slutvärded bokstaven r

for i in range(y,r): # Upprepar i (koden) för (y-r gånger)
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut
        plt.plot (x,y, '*r')
    if i%f == 0:  # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print ("birr") # Om talet stämmer så skrivs birr ut
        plt.plot (x,y, '*b')
    else:    
        print(i, end =" ") # printar i horisontellt
plt.grid() # målar ut linjer i ett diagram.
plt.show() # gör linjer i diagramet.
# uppgift a

x = 0.5 # Ger bokstaven x ett värde.
y = 0.5 # Ger bokstaven y ett värde.
c = x**2+y**2 # Ger variabeln c värdet x^2 + y^2.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.

# uppgift b 

x = 1 # Ger bokstaven x ett värde.
y = 1 # Ger bokstaven y ett värde.
c = x**2+y**2 # Ger variabeln c värdet x^2 + y^2.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.

# uppgift c

x = 0.5 # Ger bokstaven x ett värde.
y = 0.5 # Ger bokstaven y ett värde.
c = x**2+y**2 # Ger variabeln c värdet x^2 + y^2.
p = c**0.5 # Använder min c formel för att ta roten ur altså c^0.5.
print (p) # Ger mig p i skriftform.


# uppgift d

import random as rnd  # Importar random som rnd altså ger random aliaset rng.
import matplotlib.pyplot as plt # importar matplotlib.pyplot som plt, ger värde.
for n in range (50): # Upprepar x 50 gånger.
    x = rnd.uniform(-1,1) #Tildlelar x ett slumptal mellan -1 och 1.
    y = rnd.uniform(-1,1) #Tildlelar y ett slumptal mellan -1 och 1.
    print(x,y) # Skriver ut värdet på x och y.


# uppgift e
inne = 0 # Inne är en variabel för alla pilar som landar inne i cirkeln.
f = 0 # är en variabel som indikerar om pilen är innanför eller utanför.
import random as rnd # ger "random" namnet rnd
for n in range (100): # Upprepar n 100 gånger altså upprepar allt innom ranged 100 gånger
    x = rnd.uniform(-1,1) # Tildlelar x ett slumptal mellan -1 och 1.
    y = rnd.uniform(-1,1) # Tildlelar y ett slumptal mellan -1 och 1.
    f = x**2+y**2 # Tilldelar variablen f värdet x^2 + y^2
    if f <=1: # Om f (x^2+y^2) är mindre eller = med 1 så skall (inne) adera 1 pil (om pilen är i cirkeln så adderas 1)
      inne = inne +1 # hör ihop med raden över men om påståendet stämmer så adderas 1 på vad inne var före (börjar från 0 och slutar vid 100)

print(inne/n) # Skriver ut vad inne blev / antalet ex pilar kastade

# uppgift f
# Svarat från e gånger 4 narmar sig (pi) statistiskt sett.
# eftersom det är cirkels area.


# uppgift g
import random as rnd # ger "random" namnet rnd
import matplotlib.pyplot as plt # ger "matplotlib.pyplot" namnet plt
for n in range (100): # Upprepar n 100 gånger altså upprepar allt innom ranged 100 gånger
    x = rnd.uniform(-1,1) # Tildlelar x ett slumptal mellan -1 och 1.
    y = rnd.uniform(-1,1) # Tildlelar y ett slumptal mellan -1 och 1.
    if x**2+y**2 <=1: # kollar för alla värden på x,y om det är <= 1 eller inte.
      plt.plot (x,y, '*r') # ger alla tal <= 1 (alla pilar inne i cirkeln) färjen röd i diagramet.
    else: 
      plt.plot (x,y, '*b') # ger alla tal över 1 (alla pilar utanför cirkeln) färjen blå i diagramet.
plt.grid() # målar ut linjer i ett diagram.
plt.show() # visar diagramet.

# uppgift h
# ju mindre radie = mer % av kasten hamnar utanför och (1) är den största radien.


# uppgift 2 (a)

for i in range(1,101): #Upprepar i 100 gånger eller då all kod 100 gånger
    print(i, end =" ") # Print skriver ut i och end ändrar hur det skrivs ut istället för allt vertikalt så skrivs koden horisontellt.

# uppgift b

for i in range(1,101): #Upprepar i 100 gånger.
   
    if i%5 == 0: # Om 5 gångras med något och det blir 0 över så stämmer påståended ex 11 då blir det 10 och 1 över altså stämmer det bara när inget blir över.
        print("burr") # skriver ut burr om påståendet stämmer.
    else:    
        print(i, end =" ") # skriver ut i och skriver svaret horisontellt.

# Upgifft c

g = float(input("tal")) # Gör en input (valfritt tal).
for i in range(1,101): # Upprepar i (koden) fån 1 - 101 .
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut
    else:    
        print(i, end =" ") # skriver ut i och svaret är horisontellt

# Uppgift d

g = float(input("talet burr")) # Gör en input (valfritt tal).
f = float(input("talet birr")) # Gör en input (valfritt tal).
for i in range(1,101): # Upprepar i (koden) fån 1 - 101 .
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut.

    if i%f == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print ("birr") # Om påståendet stämmer så skrivs birr ut.
        
    else:    
        print(i, end =" ") # Skriver ut i horisontellt.

# Uppgift e

g = float(input("talet burr")) # Implementar g som burr altså vilken multiple burr ska vara.
f = float(input("talet birr")) # Implementar f som birr altså vilken multiple birr ska vara.
y = int(input("start")) # Ger startvärded bokstaven y.
r = int(input("slut")) # Ger slutvärded bokstaven r

for i in range(y,r): # Upprepar i (koden) för (y-r gånger)
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut

    if i%f == 0:  # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print ("birr") # Om talet stämmer så skrivs birr ut
        
    else:    
        print(i, end =" ") # printar i horisontellt

# Som förbättring så skulle man kunna ha med mer tal exempel negativa tal, decimaltal eller upphöjt.
# eftersom det gör koden mer flexibel.
# men jag kommer att fokusera på att även göra ett diagram så det ser tydligt ut.

# Under så är ett misslyckat försök av att få ett fungerande diagram
import matplotlib.pyplot as plt
g = float(input("talet burr")) # Implementar g som burr altså vilken multiple burr ska vara.
f = float(input("talet birr")) # Implementar f som birr altså vilken multiple birr ska vara.
y = int(input("start")) # Ger startvärded bokstaven y.
r = int(input("slut")) # Ger slutvärded bokstaven r

for i in range(y,r): # Upprepar i (koden) för (y-r gånger)
    
    if i%g == 0: # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print("burr") # Om påståendet stämmer så skrivs burr ut
        plt.plot (x,y, '*r')
    if i%f == 0:  # Om talet du väljer inte har något över i en multiple så stämmer påståendet.
        print ("birr") # Om talet stämmer så skrivs birr ut
        plt.plot (x,y, '*b')
    else:    
        print(i, end =" ") # printar i horisontellt
plt.grid() # målar ut linjer i ett diagram.
plt.show() # gör linjer i diagramet.
