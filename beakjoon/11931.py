import sys

input = sys.stdin.read().strip().split()
N = int(input[0])
a = list(map(int, input[1:N + 1]))
A = sorted(a, reverse=True)
for i in A:
    print(i)