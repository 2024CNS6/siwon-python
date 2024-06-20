a=input()
b=input()
c=input()
dic={
    'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4', 'green':'5', 'blue':'6', 'violet':'7', 'grey':'8', 'white':'9'
}
num=int(dic[a]+dic[b])
if c=='black':
    print(num*1)
elif c=='brown':
    print(num*10)
elif c=='red':
    print(num*100)
elif c=='orange':
    print(num*1000)
elif c=='yellow':
    print(num*10000)
elif c=='green':
    print(num*100000)
elif c=='blue':
    print(num*1000000)
elif c=='violet':
    print(num*10000000)
elif c=='grey':
    print(num*100000000)
elif c=='white':
    print(num*1000000000)