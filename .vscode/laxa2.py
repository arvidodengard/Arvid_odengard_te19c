# Uppgift 1

a = float(input("valfritt tal"))

if a > 0:
    print("possetivt")

elif a == 0:
    print("noll")

elif a < 0:
    print("negativt")

# Uppgift 3

a = float(input("Valfritt tal nummer 1"))

b = float(input("Valfritt tal nummer 2"))

if a > b:
    print("Tal nummer 1 är störst")

elif b > a:
    print("Tal nummer 2 är störst")

# Uppgift 4



a = float(input("hur många grader"))

if a < 0:
    print("ej definerat")

elif a == 90:
    print("rät vinkel")

elif a > 90 and a < 180:
    print("trubig vinkel")

elif a > 0 and a < 90:
    print("spetsig vinkel")

elif a == 180:
    print("rak vinkel")

elif a > 180 and a < 360:
    print("konvex vinkel")

elif a == 360:
    print("hel vinkel")

    
    # Uppgift 6
    

a = float(input("hur många grader"))

b = float(input("hur många grader"))

c = float(input("hur många grader"))

if a == 90:
    print("vinkel a är rät")

elif b == 90:
    print("vinkel b är rät")

elif c == 90:
    print("vinkel c är rät")

elif a != 90:
 print("har ingen rät vinkel")
    
