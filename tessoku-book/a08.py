h, w = map(int, input().split())

cumulative_sum = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    x = list(map(int, input().split()))

    for j in range(1, w + 1):
        cumulative_sum[i][j] = x[j - 1]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        cumulative_sum[i][j] += cumulative_sum[i][j - 1]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        cumulative_sum[i][j] += cumulative_sum[i - 1][j]

q = int(input())

for _ in range(q):
    a, b, c, d = map(int, input().split())

    answer = (
        cumulative_sum[c][d]
        - cumulative_sum[a - 1][d]
        - cumulative_sum[c][b - 1]
        + cumulative_sum[a - 1][b - 1]
    )

    print(answer)