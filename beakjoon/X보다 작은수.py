a, b=map(int, input().split())
c = input().split()
for i in range(a):
    if int(c[i]) < b:
        print(c[i], end=' ')