def check_padaeng_happy(T, N, F):
    total_time = sum(F)
    if total_time >= T:
        return "Padaeng_i Happy"
    else:
        return "Padaeng_i Cry"
T = int(input())
N = int(input())
F = list(map(int, input().split()))
print(check_padaeng_happy(T, N, F))
