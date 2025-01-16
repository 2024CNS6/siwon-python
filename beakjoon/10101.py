a=int(input())
b=int(input())
c=int(input())
if a==60 and b==60 and c==60:
    print("Equilateral")
elif a+b+c==180 and (a==c or b==c or b==a):
    print("Isosceles")
elif a+b+c==180 and a!=c and b!=a and c!=b:
    print("Scalene")
else:
    print("Error")