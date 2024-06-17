import sys
input = sys.stdin.readline
n=int(input())
p=0
for i in range(n):
    if i<n-1:
        a=int(input())
        p+=a-1
    elif i==n-1:
        a=int(input())
        p+=a
print(p)