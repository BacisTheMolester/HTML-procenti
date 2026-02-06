def vid_aritmētiskais():
 y = int(input("Cik sk. "))
 o = 0

 for i in range(y):
     i += 1
     x = int(input(f"{i} sk. "))
     o += x

 z = o / y
 print(f"Ciparu rindas vid. aritmētiskais ir {z}")

def kvadrāta_laukums():
    z = 0
    x = int(input("Iraksti sk. "))
    z = x * x
    print(z)
