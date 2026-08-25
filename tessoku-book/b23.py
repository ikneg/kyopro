import math, sys
input = sys.stdin.readline

N = int(input())
cities = [[0, 0] for _ in range(N)]
dp = [[10 ** 18] * N for _ in range(1 << N)]
dp[1][0] = 0

for i in range(N):
    x, y = map(int, input().split())
    cities[i][0] = x
    cities[i][1] = y

for i in range(1 << N):
    for j in range(N):
        if dp[i][j] == 10 ** 18:
            continue

        for k in range(N):
            if (i >> k) & 1:
                continue

            next = i | (1 << k)

            distance = math.dist(cities[j], cities[k])

            dp[next][k] = min(dp[next][k], dp[i][j] + distance)

maxdayo = (1 << N) - 1
ans = 10 ** 18

for i in range(N):
    distance = math.dist(cities[i], cities[0])
    ans = min(ans, dp[maxdayo][i] + distance)
print(ans)
