a = input().split(':')
b = input().split(':')
H, M, S = int(a[0]), int(a[1]), int(a[2])
h, m, s = int(b[0]), int(b[1]), int(b[2])
sumS = H * 3600 + M * 60 + S
sums = h * 3600 + m * 60 + s
num = sums - sumS
if num < 0:
    num += 24 * 3600
numH = num // 3600
num %= 3600
numM = num // 60
num %= 60
print(f"{numH:02}:{numM:02}:{num:02}")