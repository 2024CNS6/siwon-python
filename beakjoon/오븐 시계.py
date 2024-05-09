hour, minute = map(int, input().split())
a = int(input())

minute += a

hour += minute // 60
minute %= 60
if hour >=24:
    hour -=24

print(hour, minute)