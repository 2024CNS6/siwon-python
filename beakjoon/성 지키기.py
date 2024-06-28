N, M = map(int, input().split())
castle = [input().strip() for _ in range(N)]
row = 0
col = 0
for i in range(N):
    if 'X' not in castle[i]:
        row += 1
for j in range(M):
    if all(castle[i][j] == '.' for i in range(N)):
        col += 1
print(max(row, col))