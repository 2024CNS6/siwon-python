N=int(input())
for i in range(N):
    a = input()
    b=list(a)
    for j in range(len(b)):
        if b[j] == 'S':
            print(a)