a, b = map(int, input().split())
c =[]
for i in range(1, a+1):
    c.append(i)
for j in range(b):
    d, e = map(int, input().split())
    c[d-1:e] = reversed(c[d-1:e])
print(*c)