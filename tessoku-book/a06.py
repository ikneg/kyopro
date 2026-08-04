n, q = map(int, input().split())
a = list(map(int, input().split()))
cumulative_sum = [0] * (n+1)
sum_temp = 0
for i in range(n):
    sum_temp += a[i]
    cumulative_sum[i+1] = sum_temp

for i in range(q):
    a, b = map(int, input().split())

    print(cumulative_sum[b] - cumulative_sum[a-1])
