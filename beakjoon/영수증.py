a = int(input())
b = int(input())
num = 0
for i in range(b):
    c, d = map(int, input().split())
    num += c * d

if num == a:
    print("Yes")
else:
    print("No")