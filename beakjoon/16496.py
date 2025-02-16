import sys
input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
num = data[1:]
num = list(map(str, num))

S = sorted(num, key=lambda x: x * 10, reverse=True)

result = ''.join(S)

if result[0] == '0':
    result = '0'

print(result)