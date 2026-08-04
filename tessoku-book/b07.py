t = int(input())
n = int(input())

cumulative_sum = [0] * (t + 1)

for i in range(n):
    l, r = map(int, input().split())
    cumulative_sum[l] += 1
    cumulative_sum[r] -= 1

for i in range(t):
    cumulative_sum[i+1] += cumulative_sum[i]
    print(cumulative_sum[i])