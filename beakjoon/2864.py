a, b =input().split()
mina= ''
minb= ''
for i in range(len(a)):
    if a[i]=='5':
        mina+= '5'
    elif a[i]=='6':
        mina+= '5'
    else:
        mina+=a[i]
for j in range(len(b)):
    if b[j]=='5':
        minb+= '5'
    elif b[j]=='6':
        minb+= '5'
    else:
        minb+=b[j]

maxa=''
maxb=''
for i in range(len(a)):
    if a[i]=='5':
        maxa+= '6'
    elif a[i]=='6':
        maxa+= '6'
    else:
        maxa+=a[i]
for j in range(len(b)):
    if b[j]=='5':
        maxb+= '6'
    elif b[j]=='6':
        maxb+= '6'
    else:
        maxb+=b[j]
print(min(int(a), int(mina)) + min(int(b), int(minb)), max(int(a), int(maxa)) + max(int(b), int(maxb)))