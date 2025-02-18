N = int(input())
s = input()

sum = 0
for i in s:
    sum += ord(i) - 64
print(sum)