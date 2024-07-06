n = int(input())

original = n
count = 0

while True:
    a = n // 10
    b = n % 10
    sum = a + b
    n = (b * 10) + (sum % 10)

    count += 1
    if n == original:
        break
print(count)
