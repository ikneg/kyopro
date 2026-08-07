n, k = map(int, input().split())
a = list(map(int, input().split()))

half_before = a[:n//2]
half_after = a[n//2:]

before_sum = [0] * (1 << (n//2))
after_sum = [0] * (1 << (n - (n//2)))

for bit in range(1 << (n//2)):
    sum_temp = 0
    for i in range(n//2):
        if bit & (1 << i):
            sum_temp += half_before[i]
    before_sum[bit] = sum_temp

for bit in range(1 << (n - (n//2))):
    sum_temp = 0
    for i in range(n - (n//2)):
        if bit & (1 << i):
            sum_temp += half_after[i]

    after_sum[bit] = sum_temp


after_sum = set(after_sum)

for i in before_sum:
    if k - i in after_sum:
            print('Yes')
            break
else:
    print('No')
