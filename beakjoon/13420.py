n=int(input())
for i in range(n):
    a=list(input().split())
    if a[1]=='+':
        if int(a[0])+int(a[2])==int(a[4]):
            print('correct')
        else:
            print('wrong answer')
    elif a[1]=='-':
        if int(a[0])-int(a[2])==int(a[4]):
            print('correct')
        else:
            print('wrong answer')
    elif a[1]=='*':
        if int(a[0])*int(a[2])==int(a[4]):
            print('correct')
        else:
            print('wrong answer')
    elif a[1]=='/':
        if int(a[0])//int(a[2])==int(a[4]):
            print('correct')
        else:
            print('wrong answer')