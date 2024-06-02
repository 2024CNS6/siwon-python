n = int(input())
array_a = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    low = 0
    high = len(array_a) - 1

    while low <= high:
        mid = (low + high) // 2
        if array_a[mid] == target:
            print(1)
            break
        elif array_a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if low > high:
        print(0)
