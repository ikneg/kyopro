n, k = map(int, input().split())
a = list(map(int, input().split()))

right = 0
ans = 0

for left in range(n):
    while right < n - 1 and a[right+1]-a[left] <= k:
        right += 1
    ans += right - left

print(ans)
