N=int(input())
sum=0
for i in range(N):
    a, b=map(int,input().split())
    if a==136:
        sum+=1000
    elif a==142:
        sum+=5000
    elif a==148:
        sum+=10000
    elif a==154:
        sum+=50000
print(sum)