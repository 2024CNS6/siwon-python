n=int(input())
for i in range(n):
    a=input().strip()
    if a.lower()==a.lower()[::-1]:
        print('Yes')
    else:
        print('No')