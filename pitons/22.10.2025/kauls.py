import time
import random

def kauliņš():
    print("Kauliņš tiek mests!")
    x = random.randrange(1, 6)
    time.sleep(0.5)
    print(f"Uzmet {x}\n")
    return x

def spēlētājs():
    print("\n1. spēlētājs met kauliņu")
    p1 = kauliņš()
    print("\n2. spēlētājs met kauliņu")
    p2 = kauliņš()
    y = p1 - p2
    if y > 0:
         print("Uzvar 1. spēlētājs\n")
    elif y == 0:
         print("Neizšķirts\n")
    else:
         print("Uzvar 2. spēlētājs\n")

spēlētājs()
        

