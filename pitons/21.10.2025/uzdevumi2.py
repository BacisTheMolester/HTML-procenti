import random
import time

def īsais_gājiens():
 x = random.randrange(1, 50)
 z = 0
 i = 0
 while True:
    i += 1
    if z == 1 or z == 0:
       z += 1
    elif z == 2:
       z -= 1
    y = int(input(f"{z}. spēlētājs min: "))
    if y == x:
       print(f"{z}. spēlētājs uzmin {i} gājienos")
       break
    elif y > x:
       print("Par lielu!")
    else:
       print("Par mazu!")

def ātrumu_spēle():
   print("Šaujies!")
   input("Spied lai sāktu..")

   gaidisana = random.uniform(6, 7)
   time.sleep(gaidisana)

   print("Spied ENTER!")
   sakums = time.perf_counter()

   input()
   beigas = time.perf_counter()

   reakcijas_laiks = beigas - sakums
   print(f"Tavs laiks ir {reakcijas_laiks * 1000:.0f} ms")

ātrumu_spēle()