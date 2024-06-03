a=int(input())
b=int(input())
c=int(input())
if a+b==c or a+c==b or b+c==a:
    print("1")
elif a+b!=c or a+c!=b or b+c!=a:
    print("0")
else:
    print("")