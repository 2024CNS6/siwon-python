S = list(map(int, input().split()))
T = list(map(int, input().split()))
if sum(S)>sum(T):
    print(sum(S))
elif sum(T)>sum(S):
    print(sum(T))
else:
    print(sum(S))