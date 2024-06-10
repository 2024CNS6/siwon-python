N = int(input())
for i in range(N, 3, -1):
    a = str(i)
    b = True
    for j in a:
        if j != '4' and j != '7':
            b = False
            break
    if b:
        print(i)
        break