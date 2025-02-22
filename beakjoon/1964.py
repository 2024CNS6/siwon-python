def five(n):
    a = 5
    aup = 7
    for i in range(2, n + 1):
        a += aup
        aup += 3
    return a % 45678

n = int(input())
print(five(n))