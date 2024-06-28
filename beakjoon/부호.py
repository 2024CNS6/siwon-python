import sys
for _ in range(3):
    N = int(sys.stdin.readline())
    num=0
    for i in range(N):
        a = int(sys.stdin.readline())
        num+=a
    if num==0:
        print("0")
    elif num>0:
        print("+")
    elif num<0:
        print("-")