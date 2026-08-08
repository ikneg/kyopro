def print_2d(list_2d):
    for content in list_2d:
        print(*content)
    print()

n = int(input())

p = [0] * (n + 2)
a = [0] * (n + 2)
dp = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(1, n+1):
    p[i], a[i] = map(int, input().split())

for length in range(n - 2, -1, -1):
    for l in range(1, n - length + 1):
        r = l + length

        score1 = 0
        score2 = 0

        if l <= p[l - 1] <= r:
            score1 = a[l - 1]

        if l <= p[r + 1] <= r:
            score2 = a[r + 1]

        if l == 1:
            dp[l][r] = dp[l][r + 1] + score2

        elif r == n:
            dp[l][r] = dp[l - 1][r] + score1

        else:
            dp[l][r] = max(
                dp[l - 1][r] + score1,
                dp[l][r + 1] + score2
            )

answer = 0
for i in range(1, n + 1):
    answer = max(answer, dp[i][i])

print(answer)