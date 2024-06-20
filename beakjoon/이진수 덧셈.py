import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
results = []
index = 1
for _ in range(n):
    a = data[index]
    b = data[index + 1]
    num1 = 0
    num2 = 0
    for char in a:
        num1 = num1 * 2 + int(char)
    for char in b:
        num2 = num2 * 2 + int(char)
    total = num1 + num2
    if total == 0:
        results.append("0")
    else:
        binary_result = ""
        while total > 0:
            binary_result = str(total % 2) + binary_result
            total //= 2
        results.append(binary_result)
    index += 2
for result in results:
    print(result)