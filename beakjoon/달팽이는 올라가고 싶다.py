A, B, V = map(int, input().split())
if (V - B) % (A - B) == 0:
    days = (V - B) // (A - B)
else:
    days = (V - B) // (A - B) + 1
print(days)