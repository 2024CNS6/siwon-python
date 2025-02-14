import sys

input = sys.stdin.read
a = input().splitlines()
n = int(a[0])
l = []
for i in range(1, n + 1):
    l.append(int(a[i]))
l.sort()
for i in l:
    print(i)