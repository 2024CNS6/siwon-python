while True:
    num = 0
    a=input()
    if a=='0':
        break
    else:
        num+=len(a)+1
        for i in range(len(a)):
            if a[i]=='1':
                num+=2
            elif a[i]=='0':
                num+=4
            else:
                num+=3
        print(num)