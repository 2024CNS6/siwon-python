N=int(input())
L=[]
for i in range(N):
    a, b=map(int, input().split())
    L.append(a*b)
print(max(L))