n = int(input())
h = list(map(int, input().split()))
dp = [0] * (n)

for i in range(n-1):
    if i == 0:
        step = dp[i] + abs(h[i+1] - h[i])
        dp[i+1] = step
    else:
        step  = dp[i] + abs(h[i+1] - h[i])
        skip = dp[i-1] + abs(h[i+1] - h[i-1])
        dp[i+1] = min(step, skip)

print(dp[n-1])
