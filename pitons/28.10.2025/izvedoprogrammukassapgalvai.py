s = input("Teksts: \n")

vardu_sk = len(s.split())
burtu_sk = len(s)
burtu_a_sk = s.count('a')
if 'Pythone' == s:
 print("Ir varda")

print(f"Vārdu skaits {vardu_sk}", "\n", f"Burtu skaits {burtu_sk}", '\n', f"Burtu a skaits {burtu_a_sk}")