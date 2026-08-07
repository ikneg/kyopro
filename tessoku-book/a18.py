n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (s+1) for _ in range(69)]
dp[0][0] = 1
s_clone = n

for i in range(n):
    for j in range(s+1):
        if dp[i][j] == 1:
            step_length = a[i]
            if j+step_length <= s:
                dp[i+1][j+step_length] = 1
            dp[i+1][j] = 1


for i in range(n+1):
    if dp[i][s] == 1:
        print("Yes")
        break
else:
    print('No')
