a, b = map(int, input().split())
a/=60
a = float(a)
b = float(b)
c = a/b
if a>=1000:
    a/=1000
    print(f"{c:.2f}km/min")
else:
    print(f"{c:.2f}m/min")

#a와 b를 입력 받으면 실수로 바꾸어 주어야지 뒤에 있는 소수 점 뒷자리가 나온다