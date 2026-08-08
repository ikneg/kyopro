import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

dp = [[0] * 1009 for _ in range(1009)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 2
    else:
        dp[i][i+1] = 1

for LEN in range(2, n):
    for l in range(0, n - LEN):
        r = l + LEN

        if s[l] == s[r]:
            dp[l][r] = max(dp[l][r-1], dp[l+1][r], dp[l+1][r-1] + 2)
        else:
            dp[l][r] = max(dp[l][r-1], dp[l+1][r])  

print(dp[0][n-1])
