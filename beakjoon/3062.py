n=int(input())
sum=0
for i in range(n):
    a=input()
    sum=int(a)+int(a[::-1])
    if str(sum)==str(sum)[::-1]:
        print("YES")
    else:
        print("NO")