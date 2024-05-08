T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    result = pow(a, b, 10)
    print(result if result != 0 else 10)