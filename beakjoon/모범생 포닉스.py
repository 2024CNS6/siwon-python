N=int(input())
a=list(map(int,input().split()))
c=(N-1)*8+sum(a)
print(c//24, c%24)