# import sys
# input = sys.stdin.readline()

# def print_2d(list_2d):
#     for content in list_2d:
#         print(*content)

s = input().strip()
t = input().strip()

dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

for i in range(1, len(s)+1):
    dp[0][i] = i

for j in range(1, len(t)+1):
    dp[j][0] = j

for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:     
            dp[j][i] = min(dp[j-1][i] + 1, dp[j][i-1] + 1, dp[j-1][i-1])
        else:
            dp[j][i] = min(dp[j-1][i] + 1, dp[j][i-1] + 1, dp[j-1][i-1] + 1)

print(dp[len(t)][len(s)])
