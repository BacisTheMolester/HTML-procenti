y = 0

while True:
    x = int(input("Ieavadi skaitli: "))
    y += x
    if x == 0:
        print(y)
        break
    elif x < 0:
        print("Ievadi pozitīvu saitli")
        y = 0
