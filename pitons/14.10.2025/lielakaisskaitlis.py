x = int(input("Ievadi 1sk.: "))
y = int(input("Ievadi 2sk.: "))
z = int(input("Ievadi 3sk.: "))

if x > z and x > y:
    print(f"Lielākais skaitlis ir {x}")
elif z > x and z > y:
    print(f"Lielākais skaitlis ir {z}")
else:
    print(f"Lielākais skaitlis ir {y}")