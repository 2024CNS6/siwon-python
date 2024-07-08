n=int(input())
for i in range(n):
    a=list(input().split())
    l = []
    for j in range(len(a)):
        l.append(a[j][::-1])
    print(*l)