# N=int(input())
# Y=0
# a = list(map(int, input().split()))
# for i in range(N):
#     if a[i]<30:
#         Y+=10
#     elif 30<=a[i]<120:
#         Y+=30
# M=0
# for i in range(N):
#     if a[i]<60:
#         M+=15
#     elif 60<=a[i]<120:
#         M+=30
# if Y>M:
#     print("M", M)
# elif Y<M:
#     print("Y", Y)
# else:
#     print("Y", "M", Y)
import math
N = int(input())
a = list(map(int, input().split()))
Y = 0
M = 0
for i in a:
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15
if Y < M:
    print(f"Y {Y}")
elif Y > M:
    print(f"M {M}")
else:
    print(f"Y M {Y}")