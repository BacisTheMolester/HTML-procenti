while True:
    C = input("Ievadi skaitli uz celsijas: ")
    F = float(C) * 1.8 + 32
    print(F)
    if C == "beigas":
        print("Beigas!")
        break