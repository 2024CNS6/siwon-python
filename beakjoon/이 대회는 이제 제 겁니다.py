A, P, C = map(int, input().split())

max_prize_division_1 = A + C
max_prize_division_2 = P
max_prize = max(max_prize_division_1, max_prize_division_2)

print(max_prize)