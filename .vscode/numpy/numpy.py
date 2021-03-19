# Uppgift 1
import numpy as np 
 
array1 = np.arange(1,11)
 
print(array1)
 
# B 
 
array2 = np.arange(-10,11)
 
print(array2)
 
# Uppgift 2
 
import numpy as np 
 
array3 = np.arange(1,11)
 
print(array3*10)
 
# Uppgift 3
 
import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0,11)
 
def f(x):
    y = 3*x + 1 
    return y
 
 
plt.plot(f(x))
plt.title("function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
 
# Uppgift 4
 
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2,3)
 
def f(x):
    y = x**2 - 1
    return y
 
 
plt.plot(f(x))
plt.title("function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


