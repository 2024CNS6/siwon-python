num = 0
num1=0
for i in range(9):
    a = int(input())
    if a > num:
        num = a
        num1 = i+1
print(num)
print(num1)