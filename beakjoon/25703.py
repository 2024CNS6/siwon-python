a=int(input())
print('int a;')
for i in range(1, a+1):
    if i==1:
        print(f'int {"*"*i}ptr = &a;')
    elif i==2:
        print(f'int {"*" * i}ptr{i} = &ptr;')
    else:
        print(f'int {"*"*i}ptr{i} = &ptr{i-1};')