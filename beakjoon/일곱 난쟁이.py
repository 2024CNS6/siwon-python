l = []
for i in range(9):
    a = int(input())
    l.append(a)
h = sum(l)
found = False
for i in range(8):
    for j in range(i + 1, 9):
        if h - l[i] - l[j] == 100:
            f1, f2 = l[i], l[j]
            found = True
            break
    if found:
        break
D = [d for d in l if d != f1 and d != f2]
D.sort()
for k in D:
    print(k)
