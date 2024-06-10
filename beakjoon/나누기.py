N = int(input())
F = int(input())
temp = (N // 100) * 100
while temp % F != 0:
    temp += 1
print(f'{temp % 100:02d}')