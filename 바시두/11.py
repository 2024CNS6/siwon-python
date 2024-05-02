a, b, ye, n = "", "", "양예성", int(input())
for i in range(n):
    if (i%2 == 0): a += ye[i%3]
    else: b += ye[i%3]
print(f"{a}\n{b}")

#양예성을 어떻게 나눠서 출력을 해야 할지 몰랐던 것 같다.
#\n을 사용하여 줄바꿈을 해주면 알맞게 출력을 할 수 있다.