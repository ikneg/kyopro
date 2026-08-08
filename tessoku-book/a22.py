N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N

for index in range(0, N-1):
    a_index = A[index]-1
    b_index = B[index]-1
    dp[a_index] = max(dp[index] + 100, dp[a_index])
    dp[b_index] = max(dp[index] + 150, dp[b_index])

print(dp[N-1])
