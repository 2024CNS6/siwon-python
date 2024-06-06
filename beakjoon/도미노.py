N = int(input())
total_score = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        total_score += (i + j)
print(total_score)
