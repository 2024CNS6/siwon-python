a=input()
L=[]
for i in range(len(a)):
    L.append(a[i])
L.pop(0)
L.pop(-1)
print("h"+"e"*len(L)*2+"y")