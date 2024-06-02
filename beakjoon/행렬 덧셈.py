n, m = map(int, input().split())

matrix_a = []
for _ in range(n):
    matrix_a.append([int(x) for x in input().split()])

matrix_b = []
for _ in range(n):
    matrix_b.append([int(x) for x in input().split()])

result_matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

for row in result_matrix:
    print(" ".join([str(x) for x in row]))