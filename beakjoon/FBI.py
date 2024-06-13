l = []
for i in range(5):
    a = input()
    l.append(a)
found = False
for i in range(5):
    if "FBI" in l[i]:
        print(i + 1, end=' ')
        found = True
if not found:
    print("HE GOT AWAY!")