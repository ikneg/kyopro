n, m = map(int, input().split())
a = list(map(int, input().split()))
a_copy = a[:]
b = list(map(int, input().split()))
ans = 0
ans2 = 0

a[0] += 1
ans2 += 1
for i in range(1, n):
    if (a[i-1] + a[i]) % 2 != b[i-1]:
        a[i] += 1
        ans2 += 1

a = a_copy[:]
for i in range(1, n):
    if (a[i-1] + a[i]) % 2 != b[i-1]:
        a[i] += 1
        ans += 1
print(min(ans, ans2))