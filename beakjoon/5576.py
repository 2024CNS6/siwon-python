W=[]
K=[]
w=0
k=0
for i in range(10):
    W.append(int(input()))
for j in range(10):
    K.append(int(input()))
for _ in range(3):
    w+=max(W)
    W.remove(max(W))
for _ in range(3):
    k+=max(K)
    K.remove(max(K))
print(w,k)