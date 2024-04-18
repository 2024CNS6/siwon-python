n = int(input())
s = 0
while n>0:
    if n%5 == 0:
        s += n//5
        n = 0
        break
    n -= 3
    s += 1
if n<0:
    s = -1
print(s)