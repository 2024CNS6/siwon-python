import sys
input = sys.stdin.read
data = input().split()
T = int(data[0])
results = []
for i in range(1, T + 1):
    N = int(data[i])
    str_n = str(N)
    length = len(str_n)
    for j in range(length - 1, 0, -1):
        if int(str_n[j]) >= 5:
            str_n = str_n[:j - 1] + str(int(str_n[j - 1]) + 1) + '0' * (length - j)
        else:
            str_n = str_n[:j] + '0' * (length - j)
    results.append(str_n)
for result in results:
    print(result)
