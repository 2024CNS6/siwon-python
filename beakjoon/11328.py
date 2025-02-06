import sys
input = sys.stdin.read

a = input().strip().split()

n = int(a[0])

index = 1
for _ in range(n):
    s1 = a[index]
    s2 = a[index + 1]
    index += 2

    if len(s1) != len(s2):
        print("Impossible")
        continue

    count1 = [0] * 26
    count2 = [0] * 26

    for i in s1:
        count1[ord(i) - ord('a')] += 1

    for i in s2:
        count2[ord(i) - ord('a')] += 1

    if count1 == count2:
        print("Possible")
    else:
        print("Impossible")