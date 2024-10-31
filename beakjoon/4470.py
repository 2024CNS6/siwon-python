n=int(input())
l=[]
for _ in range(n):
    a=input()
    l.append(a)
for i in range(1, n+1):
    print(f'{i}. {l[i-1]}')