N = int(input())
a = str(N)
l = list(a)
for i in range(len(l) - 1, 0, -1):
    if int(l[i]) >= 5:
        l[i - 1] = str(int(l[i - 1]) + 1)
        l[i] = '0'
    else:
        l[i] = '0'
s = ''.join(l)
print(int(s))