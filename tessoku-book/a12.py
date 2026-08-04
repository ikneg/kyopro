n, k = map(int, input().split())

a = list(map(int, input().split()))

l = 0
r = (10 ** 9) - 1
while l <= r:
    index = (l + r) // 2

    flyers = sum(map(lambda x: index // x, a))

    if flyers >= k:
        r = index - 1
    else:
        l = index + 1

print(l)
