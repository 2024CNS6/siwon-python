import sys
input = sys.stdin.read
a = input().strip()
while len(a) % 3 != 0:
    a = '0' + a
b = ''
i = 0
while i < len(a):
    c = a[i:i + 3]
    b += str(int(c, 2))
    i += 3
print(b)