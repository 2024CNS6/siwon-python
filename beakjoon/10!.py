N = int(input())
p=1
for i in range(1, N+1):
    p*=i
print(p//604800)