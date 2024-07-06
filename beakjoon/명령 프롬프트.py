N = int(input())
l = [input().strip() for _ in range(N)]
p = list(l[0])
for i in l[1:]:
    for j in range(len(p)):
        if p[j] != i[j]:
            p[j] = '?'
print(''.join(p))