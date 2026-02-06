import random

def skaitlis():
 for i in range(3):
     x = random.randrange(1, 100)
     print(x)
     z = random.randrange(1, 100)

 print("x ir pirmie 3 skaitļi, z ir mināmais")
 y = input("x > z vai x < z: ")

 if x > z and y == ">":
     print("pareizi")
 elif x < z and y == "<":
     print("pareizi")
 elif x > z and y == "<":
     print("nepareizi")
 elif x < z and y == ">":
     print("nepareizi")
 elif x == z:
     skaitlis()

def pārbaude():
    x = int(input("Ieraksi sk.: "))
    if x > 0:
        print("+")
    elif x < 0:
        print("-")
    else:
        print("0")

def vienāds():
    x = int(input("Ievadi 1sk.: "))
    y = int(input("Ievadi 2sk.: "))

    if x == y:
        print("vienādi")
    else:
        print("Atšķirīgi")

def masīvs():
    x = []
    for i in range( 10):
        cipars= int(input(f"ievadi {i+1} sk. "))
        x.append(cipars)
    x.sort()
    print(f"salikts no mazākā uz lielāko: {x}")
    
    mediāna = (x[4] + x[5]) / 2
    print(f"Mediāna ir {mediāna}")
    print("Pirmās 3 vērtības", x[:3])
    print("Pēdējās 3 vērtības", x[-3:])

masīvs()