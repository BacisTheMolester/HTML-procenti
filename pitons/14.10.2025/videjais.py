z = 0
y = 0

while True:
    x = int(input("Ieavadi skaitli: "))
    z += x
    if x == 0:
        y = z / 2
        print(f"Vidējais aritmētiskais ir {y}")
        break

"""
Algoritma apr.
1. Sākums
2. Ievads z = 0; y = 0
3. Nosacijumi kamēr paties ievada x, saskaita z + x, ja x = 0, tad y = z / 2,
4. Izvade y
5. Beigas

Mat. apr.
Sākums
1. z = 0; y = 0,
2. kamēr paties x = ?, z = x + z, ja x = 0, tad y = z/2
3. izvada mainīgā y vērtību
beigas
"""