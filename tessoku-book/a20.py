from sys import stdin

input = stdin.readline

s = input().strip()
t = input().strip()

dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

for i in range(len(t)):
    for j in range(len(s)):
        if s[j] == t[i]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(
                dp[i][j+1],
                dp[i+1][j]
            )

print(dp[i+1][j+1])
