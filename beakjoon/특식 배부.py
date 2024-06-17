N = int(input())
sum=0
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i]<=N:
        sum+=a[i]
    elif a[i]>N:
        sum+=N
print(sum)