a = list(range(1, 31))
for i in range(28):
    b = int(input())
    a[b-1]=0
while 0 in a:
    a.remove(0)
print(min(a))
print(max(a))
