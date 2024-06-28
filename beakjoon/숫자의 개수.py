a=int(input())
b=int(input())
c=int(input())
d=a*b*c
num=0
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
num7=0
num8=0
num9=0
for i in range(len(str(d))):
    if str(d)[i]=='0':
        num+=1
    elif str(d)[i]=='1':
        num1+=1
    elif str(d)[i]=='2':
        num2+=1
    elif str(d)[i]=='3':
        num3+=1
    elif str(d)[i]=='4':
        num4+=1
    elif str(d)[i]=='5':
        num5+=1
    elif str(d)[i]=='6':
        num6+=1
    elif str(d)[i]=='7':
        num7+=1
    elif str(d)[i]=='8':
        num8+=1
    elif str(d)[i]=='9':
        num9+=1
print(num)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
print(num9)