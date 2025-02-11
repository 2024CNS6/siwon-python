import sys
input = sys.stdin.read
data = input().strip().split()
l1 = data[0]
l2 = data[1]
sum = int(l1, 2) + int(l2, 2)
result_binary = bin(sum)[2:]
print(result_binary)