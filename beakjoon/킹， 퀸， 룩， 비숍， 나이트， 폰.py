a= list(map(int, input().split()))

b = [1, 1, 2, 2, 2, 8]

result = [b[i] - a[i] for i in range(len(a))]

print(*result)