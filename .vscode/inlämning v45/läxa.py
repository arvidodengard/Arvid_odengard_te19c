# uppgift a

x = 0.5
y = 0.5
c = x**2+y**2
p = c**0.5
print (p)

# uppgift b 

x = 1
y = 1
c = x**2+y**2
p = c**0.5
print (p)

# uppgift c

x = 0.5
y = 0.5
c = x**2+y**2
p = c**0.5
print (p)

# uppgift d

import random as rnd 
import matplotlib.pyplot as plt 
for x in range (50):
    x = rnd.uniform(-1,1)
    y = rnd.uniform(-1,1)

    plt.plot (x,y)
plt.grid()
plt.show()

# uppgift e
import random as rnd 
for x in range (100):
    x = rnd.uniform(-1,1)
    y = rnd.uniform(-1,1)
    if x**2+y**2 <=1: print (x)

# hade 26 punkter utanför och 24 innanför altså 24/50 = 0.48

# uppgift f

i = 0.48 *4
print (i)
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