import math
n=int(input())
sum=str(math.factorial(n))
i=-1
while True:
    if sum[i]=='0':
        i-=1
    else:
        print(sum[i])
        break