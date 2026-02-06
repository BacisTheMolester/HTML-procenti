def masīvs():
    x = []
    for i in range(5):
        cipars= int(input(f"ievadi {i+1} sk. "))
        x.append(cipars)
    z = sum(x)
    aritmetiskais = z / 2
    print(f"Summa {z}")
    print(f"Vid. aritmētiskais ir {int(aritmetiskais)}")

def Otrs_masīvs():
    y = int(input("Ieraksti cik skaitļus gribi ievadīt: "))
    if y == 0:
        print("Ievadi korektu skaitli.")
    x = []
    for i in range(y):
        cipars= int(input(f"ievadi {i+1} sk. "))
        x.append(cipars)
    x.sort()
    p = x[:1]
    z = x[-1 :]
    print(f"\nLielākais sk. {z}\n Mazākais sk. {p}\n Viss saraksts {x}")

Otrs_masīvs()