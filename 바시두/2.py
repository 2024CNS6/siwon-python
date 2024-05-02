N = int(input())
a = []
d = []
dic = {}
rev = {}
for i in range(N):
    name, grade = input().split()
    dic[name] = int(grade)
    rev[int(grade)] = name
    a.append(dic[name])
    d.append(rev[int(grade)])
    a.sort(reverse=True)
    d.sort(reverse=True)
for j in a:
    if j >= 90:
        print(f"{rev[j]} A")
    elif j >= 80:
        print(f"{rev[j]} B")
    elif j >= 70:
        print(f"{rev[j]} C")
    elif j >= 60:
        print(f"{rev[j]} D")
    else:
        print(f"{rev[j]} F")

# if문을 사용 하기 전에 받은 점수의 값이 큰 순서 대로 정렬을 해주고 if 문은
# 돌리게 되면 받은 점수가 큰 순서 대로 나열 된다.