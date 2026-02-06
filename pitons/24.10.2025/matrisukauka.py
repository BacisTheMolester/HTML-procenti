def izmekle(A, B): #Pārbaude
        if len(A) != len(B) or len(A[0]) != len(B[0]): 
         print("Nevar veikt darbību")
         return None

def saskaiti(A, B): #Saskaita
    izmekle(A, B)
    return [A[i][j] + B[i][j] for j in range(len(A[0])) for i in range(len(A))]

def reizinasana(A, B): #Reizina
    izmekle(A, B)
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = sum(A[i][j] * B[i][j] for k in range(len(B))) 
            row.append(s)
            C.append(row)
    return C

def druka_matricu(M):
    for r in M:
        print(" ".join(f"{x: 5}" for x in r))

A = []
B = []

print("A + B =")
druka_matricu(saskaiti(A, B))
print()
druka_matricu(reizinasana(A, B))