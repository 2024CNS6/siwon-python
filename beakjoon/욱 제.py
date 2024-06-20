A, B = map(int, input().split())
M = (B - A) / 400
probability = 1 / (1 + 10**M)
print(f"{probability:.15f}")