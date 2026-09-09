import bisect

d = int(input())
n = int(input())
m = int(input())
shop = [0, d]


for i in range(n-1):
    shop.append(int(input()))

shop.sort()
ans = 0
for i in range(m):
    t = int(input())
    r = bisect.bisect_left(shop, t)
    l = r - 1
    ans += min(shop[r] - t, t - shop[l])
print(ans)