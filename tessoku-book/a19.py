N, W = map(int, input().split())
max_value = N * 1000
inf = 10 ** 18

dp = [[inf] * (max_value + 1) for _ in range(N+1)]
dp[0][0] = 0

def print_2d(list_2d):
    for content in list_2d:
        print(*content)
    print()
for i in range(N):
    w, v = map(int, input().split())
    for j in range(max_value + 1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        if j + v <= max_value:
            dp[i+1][j+v] = min(dp[i+1][j + v], dp[i][j] + w)


for index in range(max_value, -1, -1):
    if dp[N][index] <= W:
        print(index)
        break
