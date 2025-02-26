n = int(input())
S=0
B=0
L=0
P=0
for i in range(n):
    a, b = input().split()
    if a=='STRAWBERRY':
        S += int(b)
    elif a=='BANANA':
        B += int(b)
    elif a=='LIME':
        L += int(b)
    elif a=='PLUM':
        P += int(b)
if S==5 or B==5 or L==5 or P==5:
    print('YES')
else:
    print('NO')