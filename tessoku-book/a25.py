H, W = map(int, input().split())

c = [[] for _ in range(H)]
INF = 10 ** 18
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    temp = list(input())
    c[i] = temp

for i in range(H):
    for j in range(W):
        if j < W - 1 and c[i][j + 1] == '.':
            dp[i][j+1] += dp[i][j]

        if i < H - 1 and c[i+1][j] == '.':
            dp[i+1][j] += dp[i][j]

print(dp[H-1][W-1])
