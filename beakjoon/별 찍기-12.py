N=int(input())
for i in range(1,N+1):
    print(f"{'*'*i:>{N}}")
for j in range(N-1, 0, -1):
    print(f"{'*'*j:>{N}}")