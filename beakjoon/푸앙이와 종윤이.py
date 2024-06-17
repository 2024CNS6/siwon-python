a,b=map(int,input().split())
print(100-a, 100-b, 100-(100-a + 100-b), (100-a)*(100-b), (100-a)*(100-b)//100, (100-a)*(100-b)%100)
num=str(a*b)
if len(num)==3 and num[-2]=='0':
    print(num[0], num[-1])
elif len(num)==3:
    print(num[0], num[-2]+num[-1])
elif num[-2]=='0':
    print(num[0]+num[1], num[-1])
else:
    print(num[0]+num[1], num[-2]+num[-1])