N = int(input())
P = [0] * (N + 2)
A = [0] * (N + 2)

dp = [[0] * (N + 2) for _ in range(N + 2)]

for i in range(1, N+1):
    p, a = map(int, input().split())
    P[i] = p
    A[i] = a
for LEN in range(N-2, -1, -1):
    for l in range(1, N-LEN+1):

        r = l + LEN

        score1 = 0
        score2 = 0

        if l <= P[l-1] <= r:
            score1 = A[l-1]

        if l <= P[r+1] <= r:
            score2 = A[r+1]

        if l == 1:
            dp[l][r] = dp[l][r+1] + score2

        elif r == N:
            dp[l][r] = dp[l-1][r] + score1

        else:
            dp[l][r] = max(
                dp[l-1][r] + score1,
                dp[l][r+1] + score2
            )

ans = 0
for i in range(1, N+1):
    ans = max(dp[i][i], ans)

print(ans)

