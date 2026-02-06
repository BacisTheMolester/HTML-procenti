n = int(input())

reverse = 0

while n != 0:
    last_dih = n % 10
    reverse = reverse * 10 + last_dih
    n //= 10

print(reverse)