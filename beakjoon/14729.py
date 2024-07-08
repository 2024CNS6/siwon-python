n = int(input())
l = []
for _ in range(n):
    a = float(input())
    l.append(a)
l.sort()
for i in range(7):
    print(f'{l[i]:.3f}')