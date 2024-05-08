N = int(input())

if 0 <= N <= 12:
    f = 1
    for i in range(1, N+1):
        f *= i
    print(f)
else:
    print("잘못된 입력입니다. 0부터 12 사이의 정수를 입력하세요.")