import sys
input = sys.stdin.readline
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
sorted_numbers = sorted(numbers)
for number in sorted_numbers:
    print(number)