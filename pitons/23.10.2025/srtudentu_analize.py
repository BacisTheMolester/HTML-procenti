pirmais_list = []
otrais_list = []

z = int(input("Cik studentu: "))

for i in range(z):
 p = input("Ievadi studentu vārdu: ")
 y = int(input("Ievadi atzīmi "))
 pirmais_list.append(p)
 otrais_list.append(y)

for l, j in zip(pirmais_list, otrais_list):
 print(l, j)

