from bisect import bisect_left

N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

ans = 0
for x in T:
    idx = bisect_left(S, x)

    if 0 <= idx < N and S[idx] == x:
        ans += 1

print(ans)

