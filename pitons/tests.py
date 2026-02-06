precu_skaits = int(input("Ievadi cik preces būs: "))
print("ja prece tiks atkārtoti rakstīta, raksti ciparu klāt pie preču nosaukumu, tā lai precei tiktu reģistrēta")
preces = {}

def kopsumma():
   return sum(cenas for cenas in preces.values())

def letaka_prece():
   return min(preces.items(), key= lambda x: x[1])

def dargaka_prece():
   return max(preces.items(), key= lambda x: x[1])

for i in range(1, precu_skaits+1):
 prece = input("Ievadi preces nosaukumu: ")
 cena = float(input("Ievadi cenu: "))
 preces.update({prece: cena})

letaka = letaka_prece()
dargaka = dargaka_prece()
list_kop = (letaka[1], dargaka[1])

print("\n","   ","Tabula")
for prece, cena in preces.items():
 print(f'{prece} ---- {cena}','$')
print("\n","Kopsumma ",str(kopsumma()),"$")
print("Lētākā cena ",f"{letaka[1]}",'$')
print("Dārgākā cena ",f"{dargaka[1]}",'$')
print("Kopsumma starp Dārgāko cenu un Lētāko cenu: ",f'{sum(list_kop)}',"$")