N = input().strip()
l = len(N)
a = False
for i in range(1, l):
    left = N[:i]
    right = N[i:]

    left_product = 1
    for char in left:
        left_product *= int(char)

    right_product = 1
    for char in right:
        right_product *= int(char)

    if left_product == right_product:
        a = True
        break

if a:
    print("YES")
else:
    print("NO")
