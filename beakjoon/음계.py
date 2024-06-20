a=list(map(int,input().split()))
A=0
D=0
for i in range(len(a)):
    if a[i]==i+1:
        A+=1
    elif a[i]==8-i:
        D+=1
if A==8:
    print("ascending")
elif D==8:
    print("descending")
else:
    print("mixed")