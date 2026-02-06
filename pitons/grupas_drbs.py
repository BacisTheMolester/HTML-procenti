def videjais():
    return sum(1 for atzime in saraksts.values() if atzime >= 8) / len(saraksts)
def labakais():
    return max(saraksts.items(), key= lambda x: x[1])
def vajakais():
    return min(saraksts.items(), key= lambda x: x[1])
def virs_8():
    return sum(1 for atzime in saraksts.values() if atzime >= 8)

skaits = int(input('Skolēnu sk. '))
saraksts = {}

for i in range(1, skaits+1):
    vards = input(f'{i} Skolēnu vārds: ')
    while True:
     atzime = int(input('Atzīme: '))
     if 1 <= atzime <= 10:
      saraksts[vards] = atzime
      break
     else:
      print("Kļūda radās.")

saraksts_sakartots = sorted(saraksts.items(), key=lambda x: x[1], reverse=True)

print('\n' + '-'*8)
print(" " + "Tabula")
for vards, atzime in saraksts_sakartots:
   print(f'{vards}, {atzime}')
print('\n' + f'videjais klasē {videjais()}')
print('\n' + f'labakais {labakais()}')
print('\n' + f'vajakais {vajakais()}')
print('\n' + f'virs_8 ir {virs_8()} skolēniem')