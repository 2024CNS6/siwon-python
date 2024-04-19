a, b=map(int, input().split())
c=[0 for _ in range(a)]
for i in range(b):
    d, e, f=map(int, input().split())
    for j in range(d, e+1):
        c[j-1]=f
print(*c)