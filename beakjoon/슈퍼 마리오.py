sum = 0
l = []
for _ in range(10):
    a = int(input())
    l.append(a)
Csum = 0
for i in range(len(l)):
    sum += l[i]
    if sum >= 100:
        if abs(sum - 100) < abs(Csum - 100):
            Csum = sum
        elif abs(sum - 100) == abs(Csum - 100):
            Csum = max(sum, Csum)
        break
    Csum = sum
print(Csum)