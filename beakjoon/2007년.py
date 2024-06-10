M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
m, d = map(int, input().split())
a = sum(M[:m - 1]) + d
b = w[(a - 1) % 7]
print(b)
