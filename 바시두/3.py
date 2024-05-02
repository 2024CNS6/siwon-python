a = input()
b = int(input())
z = b
for i in range(b):
    c = input()
    d = []
    d.append(c)
    for j in range(len(d)):
        if a in d[j]:
            z += 1
print(z)

# 이름이 꼭 세 글자로 정해져 있는 것은 아니므로 이름이 몇 글자던 될 수 있도록 코드를 작성해야 한다.