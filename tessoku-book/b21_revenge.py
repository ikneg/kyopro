import sys
input = sys.stdin.readline

def print_2d(list_2d):
    for item in list_2d:
        print(item)

N = int(input())
S = input().strip()

dp = [[0] * N for _ in range(N)]

#長さが1
for i in range(N):
    dp[i][i] = 1

#長さが2
for i in range(N-1):
    if S[i] == S[i+1]:
        dp[i][i+1] = 2
    else:
        dp[i][i+1] = 1

for LEN in range(2, N):
    for l in range(N-LEN):
        r = l + LEN

        if S[l] == S[r]:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1] + 2)
        else:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1])

print(dp[0][N-1])
