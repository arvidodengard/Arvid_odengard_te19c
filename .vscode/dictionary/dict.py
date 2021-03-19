# Uppgift 1
points = 0
 
course = dict(
    Ma4 = 100,
    Prog1 = 100,
    Sv2 = 100,
    Web1 = 100,
    Fys1 = 100,
    Eng6 = 100,
    Daodac1 = 100,
    Idr1 = 100,
)
 
for key in kurser: 
    points = points + course[key]
print(points)
 
# Uppgift 2
 
import random as rnd
 
kast = {
    "ett": 0,
    "två": 0,
    "tre": 0,
    "fyra": 0,
    "fem": 0,
    "sex": 0,
}
    
 
 
for i in range(100000):
    tärning = rnd.randint(1,6)
 
    if tärning == 1:
        kast["ett"] += 1
    
    elif tärning == 2:
        kast["två"] += 1
    
    elif tärning == 3:
        kast["tre"] += 1
    
    elif tärning == 4:
        kast["fyra"] += 1
    
    elif tärning == 5:
        kast["fem"] += 1
 
    elif tärning == 6:
        kast["sex"] += 1
 
print(kast)
 

# uppgift 3
pokedex = {}

indata = str(input("pokemon =  "))



with open ("pokemonlista.txt", "r") as f1:

    for i in f1:
        ( index , pokemon , typ) = line.split()
        pokedex[(pokemon)] = [index, typ]
    

    nummer = (pokedex[indata] [0])
    talang = (pokedex[indata] [1])

    print (f"typ: {talang}, index: {nummer}")

    






