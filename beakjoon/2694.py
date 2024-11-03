n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    a.sort()
    for j in range(2):
        a.remove(max(a))
    print(max(a))