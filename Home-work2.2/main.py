a1 = int(input())

a2 = 0

while a1 > 0:
    digit = a1 % 10
    a1 = a1 // 10

    a2 = a2 * 10 + digit

print(a2)
