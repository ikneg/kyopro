n, k = map(int, input().split())
a = list(map(int, input().split()))
cumulative_sum = [0] * (n + 1)

for i in range(n):
    cumulative_sum[i+1] = a[i] + cumulative_sum[i]

left = 0
ans = 0

for right in range(n):
    left = max(right, left)

    while left < n and cumulative_sum[left+1] - cumulative_sum[right] <= k:
        left += 1

    ans += left - right

print(ans)
