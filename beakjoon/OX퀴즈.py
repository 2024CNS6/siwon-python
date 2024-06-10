a = int(input())
b = [input().strip() for _ in range(a)]
for i in b:
    c = 0
    d = 0
    for j in i:
        if j == 'O':
            d += 1
            c += d
        else:
            d = 0
    print(c)
