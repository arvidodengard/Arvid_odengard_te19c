name = "Arvid"
print(f"Ditt namn är {name}")

g = 9.82


m = float(input("din vikt"))

F = m*g # 599.02

print(f"Din tyngdkraft är {F}N") #f-string 
print("Din tyngdkraft är",F,"N")

decimalTal = float(input("decimaltal"))
procent = decimalTal*100

print(f"{decimalTal} = {procent:.1f}%")
print(decimalTal,"=",round(procent),"%")

kelvin = float(input("antal kelvin"))
c = kelvin - 273.15
print(f"antal celsius{c}7")

c = float(input("antal celsius"))
k = c + 273.15
print(f"antal kelvin {k}")

a = float(input("hur många gånger per månad åker du med västrafik"))

b = a*30

if b > 775:
    print("månadskort blir billigare")


print(f"priset blir {b}")
