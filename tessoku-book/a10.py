n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
l[0] = a[0]
r[n-1] = a[n-1]

for i in range(1, n):
    l[i] = max(a[i], l[i-1])

for i in range(n-2, -1, -1):
    r[i] = max(a[i], r[i+1])

d = int(input())
for i in range(d):
    a, b = map(int, input().split())
    print(max(l[a-2], r[b]))