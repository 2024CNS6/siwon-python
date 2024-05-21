a = set()
for _ in range(10):
    b = int(input())
    c = b % 42
    a.add(c)
print(len(a))