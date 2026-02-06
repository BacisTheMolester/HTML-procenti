import re

s = input("Ievadi savu tekstu:\n")

def tirit_tekstu(s) -> list[str] :
    filtered_str = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower()
    return filtered_str

def top_n(filtrets_teksts: list[str], vards: str) -> list[tuple[str, int]]:
    skaits = filtrets_teksts.count(vards.lower())
    tabula = [(vards, skaits)]
    return tabula


filtrets_teksts = tirit_tekstu(s) 
print("Filtrēts teksts: " ,"\n", filtrets_teksts)
vards = input("Kāda vārds freq:  ")
top_vards = top_n(filtrets_teksts, vards)
print("biežākie vārdi: " ,"\n", top_vards)