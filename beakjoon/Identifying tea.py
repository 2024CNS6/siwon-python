a=int(input())
b=list(map(int,input().split()))
num=0
for i in range(len(b)):
    if b[i]==a:
        num+=1
print(num)