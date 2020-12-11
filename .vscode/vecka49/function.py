# Uppgift 1
def artimetiskt_summa(a, n, p):
    summa = 0
    i = 0
    while i < n:
        summa = summa + a
        a = a + p
        i = i + 1
    return summa

n = 10
a = 1
p = 1

print(artimetiskt_summa(a, n, p))

# uppgift b
def artimetiskt_summa(a, n, p):
    summa = 0
    i = 0
    while i < n:
        summa = summa + a
        a = a + p
        i = i + 1
    return summa

n = 100
a = 1
p = 1

print(artimetiskt_summa(a, n, p))
# Uppgift c

n = int(input("Maximalt tal:"))
a = int(input("start tal:"))
p = int(input("ökning per tal:"))

def artimetiskt_summa(a, n, p):
    summa = 0
    i = 0
    while i < n:
        summa = summa + a
        a = a + p
        i = i + 1
    return summa

print(artimetiskt_summa(a, n, p))

# Uppgift 2

n = int(input("Maximalt tal:"))

def artimetiskt_summa(a, n, p):
    summa = 0
    i = 0
    while i < n:
        summa = summa + a
        a = a + p
        i = i + 2
    return summa

a = 1
p = 2
n = 2*n+1
print(artimetiskt_summa(a, n, p))

# Uppgift b

n = int(input("Maximalt tal:"))
a = int(input("start tal:"))
n = n*2+1
def artimetiskt_summa(a, n, p):
    summa = 0
    i = 0
    while i < n:
        summa = summa + a
        a = a + p
        i = i + 2
    return summa

p = 2
print(artimetiskt_summa(a, n, p))

# Uppgift 3
tal = int(input("antal pengar:"))
tusenlappar = 0
while tal > 999.99999:
    tusenlappar = tusenlappar +1 
    tal = tal -999.99999

tvåhundralappar = 0
while tal > 199.99999:
    tvåhundralappar = tvåhundralappar +1 
    tal = tal -199.99999

tjugolappar = 0
while tal > 19.9999999:
    tjugolappar = tjugolappar +1 
    tal = tal -19.9999999

tia = 0
while tal > 9.9999999:
    tia = tia +1 
    tal = tal -9.9999999

femma = 0
while tal > 4.9999999:
    femma = femma +1 
    tal = tal -4.9999999

enkrona = 0
while tal > 0.9999999:
    enkrona = enkrona +1 
    tal = tal -0.9999999
print(tusenlappar,tvåhundralappar,tjugolappar,tia,femma,enkrona)
