import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a = math.ceil(A / C)
b = math.ceil(B / D)
c = max(a, b)
d = L - c
print(d)
