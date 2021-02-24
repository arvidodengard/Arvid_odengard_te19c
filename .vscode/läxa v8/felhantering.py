# Uppgift 1
import numpy as np
 
def distance(p1, p2):
    return np.sqrt(p1+p2)
 
print(distance(0.5,0.5))

# Uppgift 2 
def ar_fyrsiffrigt (tal):
    if tal//1000 < 10 and tal//1000 >= 1 :
        return True 
    elif tal//1000 > -10 and tal//1000 <= -1 :
        return True 
    else:
        return False 
 
testtal = [100, 231, 10000, 10001, -1000, 102313]
 
for t in testtal:
    if ar_fyrsiffrigt(t):
        print(f"{t} är fyrsiffrigt")
    else:
        print(f"{t} är inte fyrsiffrigt")

# Uppgift 3

while True:
    try:
        Måndadskort = int(input("vad kostar ett månadskort? "))
        engångskostnad = int(input("hur mycket kostar det att åka med engångskostnad"))
        antal_åk = int(input("hur många gånger vill du åka denna månad? "))
        assert Måndadskort > 0 and engångskostnad > 0 and antal_åk > 0
        break
    except AssertionError as msg:
        print(msg)
    except:
        print(print("månadskort,engångskostnad och antal_åk skall vara tal inte en string"))

if engångskostnad * antal_åk > Måndadskort:
    print("du skall ha Månadskort")

else:
    print("du ska ha engångskostnad")