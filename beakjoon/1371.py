import sys
input = sys.stdin.read

a = input().strip()

counts = [0] * 26

for i in a:
    if i.isalpha():
        counts[ord(i.lower()) - ord('a')] += 1

m = max(counts)

result = []
for j in range(26):
    if counts[j] == m:
        result.append(chr(j + ord('a')))

print(''.join(result))