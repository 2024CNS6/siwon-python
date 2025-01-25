c = [0] * 26
S = input().strip()
for i in S:
    c[ord(i) - ord('a')] += 1
print(" ".join(map(str, c)))
