n = int(input())
l = [3]
while l[-1] < n:
    l.append(2 * l[-1] + len(l) + 3)
k = len(l) - 1
while k > 0:
    a = l[k - 1]
    b = k + 3
    if n <= a:
        k -= 1
    elif n <= a + b:
        if n - a == 1:
            print('m')
        else:
            print('o')
        break
    else:
        n -= a + b
        k -= 1
if k == 0:
    print("moo"[n - 1])