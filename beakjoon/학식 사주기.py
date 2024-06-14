sum=0
M=int(input())
m=[]
for i in range(M):
    a=int(input())
    m.append(a)
S=int(input())
for i in range(S):
    b=int(input())
    sum+=m[b-1]
print(sum)