ma = -1000001
mi = 1000001
N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    if a[i] > ma:
        ma = a[i]
    if a[i] < mi:
        mi = a[i]
print(mi, ma)