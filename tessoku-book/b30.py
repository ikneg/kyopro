def power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2**i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m

        p = (p * p) % m

    return Answer


def Division(a, b, m):
    return (a * power(b, m - 2, m)) % m


H, W = map(int, input().split())

# dp = [[0] * W for _ in range(H)]
# dp[0][0] = 1

# for i in range(H):
#     for j in range(W):
#         if i < H - 1:
#             dp[i + 1][j] += dp[i][j]
#             dp[i + 1][j] %= 1000000007
#         if j < W - 1:
#             dp[i][j + 1] += dp[i][j]
#             dp[i][j + 1] %= 1000000007

# print(dp[H - 1][W - 1])

permutation = [0] * (H + W)
permutation[0] = 1

for i in range(1, H + W):
    permutation[i] = permutation[i - 1] * i % 1000000007

numerator = permutation[H + W - 2]

denominator = permutation[H - 1] * permutation[W - 1]

print(Division(numerator, denominator, 1000000007))
