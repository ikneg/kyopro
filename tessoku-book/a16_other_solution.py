n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
INF = 10 ** 18

dp = [INF] * n
dp[0] = 0

for i in range(0, n-1):
    if i < n-2:
        dp[i+1] = min(a[i] + dp[i], dp[i+1])
        dp[i+2] = min(b[i] + dp[i], dp[i+2])
    else:
        dp[i+1] = min(a[i] + dp[i], dp[i+1])

print(dp[n-1])
