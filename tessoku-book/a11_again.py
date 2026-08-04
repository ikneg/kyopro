n, x = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = n-1

while l <= r:
    index = (l + r) // 2

    if a[index] >= x:
        r = index - 1
    else:
        l = index + 1
print(l+1)
