import bisect

N = int(input())
A = list(map(int, input().split()))

l = []
dp = [0] * N

for i in range(N):
    pos = bisect.bisect_left(l, A[i])
    dp[i] = pos + 1

    if pos == len(l):
        l.append(A[i])
    else:
        l[pos] = A[i]

print(len(l))
