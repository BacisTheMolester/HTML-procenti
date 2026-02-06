a = int(input("No kura sk. "))
b = int(input("Līdz kuram sk. "))

def ir_pirmskaitlis(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % 2 == 0:
            return False
    return True

def get_pirmskailtis(a, b):
    return [n for n in range(a, b + 1) if ir_pirmskaitlis(n)]

if a > b:
    print("Kļūda radās.")
else: 
    saraksts = get_pirmskailtis(a, b)
    
    if not saraksts:
        print("Intervālā nav pirmskaitļu")
    else:
        skaits = len(saraksts)
        summa = sum(saraksts)
        atstarpes = [skaits[i + 1] - skaits[i] for i in range(skaits - 1)]
        lielaka_atstarpe = max(atstarpes) if atstarpes else 0

        print(f"Saraksts {saraksts}")
        print(f"Saraksta lielums {skaits}")
        print(f"Summa {summa}")
        print(f"Atstarpes starp sk. {atstarpes}")
        print(f"Lielākā atstarpe starp sk. {lielaka_atstarpe}")



