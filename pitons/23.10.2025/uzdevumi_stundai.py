x = []

def atlasi_pzitivus():
    pozitivie = [i for i in x if i > 0]
    summa_pirma = sum(pozitivie)
    print(f"pozitivie sk. {pozitivie}\n", f"Summa {summa_pirma}")

def analize():
    summa_otra = sum(x)
    videjais = summa_otra / len(x)
    mazakais = min(x)
    lielakais = max(x)
    print(f"Vidējais sk. {videjais}\n", f"Summa {summa_otra}\n", f"Mazākais {mazakais}, Lielākais {lielakais}\n")

def lielaki_par_videjo():
    print(x)
    vid_vertiba = sum(x) / len(x)
    virs_videja = [z for z in x if z > vid_vertiba]
    print(f"Vidējā vertiba {vid_vertiba}\n", f"Virs vidēja {virs_videja}")

def dotie_cipari():
 y = int(input("Ievadi cik sk. gribi: "))

 for i in range(y):
     p = int(input(f"{i} Skaitlis: "))
     x.append(p)
 return x

def galvena_dala():
 izvele = int(input("Ievadi kuru gribi veikt: "))
 if izvele == 1:
    dotie_cipari()
    atlasi_pzitivus()
 elif izvele == 2:
    dotie_cipari()
    analize()
 elif izvele == 3:
    dotie_cipari()
    lielaki_par_videjo()

galvena_dala()
