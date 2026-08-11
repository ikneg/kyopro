n, m = map(int, input().split())
A = [0] * m
dp = [[109] * (2 ** n) for _ in range(m+1)]
dp[0][0] = 0

for i in range(m):
    temp = list(map(int, input().split()))
    A[i] = temp

for i in range(m):
    for j in range(2 ** n):
        if dp[i][j] < 100 or j == 0:
            already = [0] * n
            for k in range(n):
                if 1 & (j >> k):
                    already[k] = 1

            for k in range(n):
                if A[i][k] > 0:
                    already[k] = 1

            ans = 0
            for k in range(n):
                if 1 & already[k]:
                    ans += 2 ** k
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            dp[i+1][ans] = min(dp[i][j]+1, dp[i+1][ans])

if dp[m][(2 ** n) - 1] > 105:
    print('-1')
else:
    print(dp[m][(2 ** n) - 1])
