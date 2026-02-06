import random

def kvadrāts():
 x = int(input("skaitlis: "))
 for i in range(1, x):
     z = i*i
     print(i, z)

def saskaite():
   x = int(input("skaitlis: "))
   for i in range(1, x):
      z = i % 2
      if z == 0:
         print(i)

def apgriešana():
   x = int(input("skaitlis: "))
   y = str(x)
   print(y[::-1])

def minēšana():
   p = 0
   for i in range(1, 11):
       skaitlis = random.randrange(1, 100)
       y = random.randrange(1, 100)
       if i == 1:
        print(f"Pirmais {skaitlis} vai nākošais būs pāra vai nepāra??")
       x = input("Raksti Pāra vai Nepāra: ")
       z = y % 2
       if x == "Pāra" and z == 0:
         p += 1
         print("Nākošais")
       elif x == "Nepāra" and z == 0:
         p -= 1
         print(f"skaitlis bija {y}")
       elif z == 1 and x == "Nepāra":
         p += 1
         print("Nākošais")
       elif x == "Pāra" and z == 1:
         p -= 1
         print(f"skaitlis bija {y}")
   print(f"skripts beidzas tu ieguvi {p} punktus")