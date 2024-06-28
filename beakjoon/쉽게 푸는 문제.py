a, b = map(int, input().split())
l = []
for i in range(1, 1000):
    for _ in range(i):
        l.append(i)
    if len(l) >= b:
        break
S = sum(l[a - 1:b])
print(S)