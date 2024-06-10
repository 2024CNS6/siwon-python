t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = (n - 1) % h + 1
    room = (n - 1) // h + 1
    print(f"{floor}{room:02d}")