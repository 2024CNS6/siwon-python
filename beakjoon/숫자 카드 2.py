import sys
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
count = {}
for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
m = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for j in a:
    if j in count:
        print(count[j], end=" ")
    else:
        print(0, end=" ")