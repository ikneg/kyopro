n = int(input())

l = 0
r = n
index = 0
while l <= r:
    index = (l + r) / 2
    result = index ** 3 + index

    if result >= n:
        r = index - 0.001
    else:
        l = index + 0.001
print(l)
