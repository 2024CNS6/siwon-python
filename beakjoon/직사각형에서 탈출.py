x, y, w, h= map(int, input().split())
num=min(x, w-x, y, h-y)
print(num)