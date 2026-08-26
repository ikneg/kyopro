N = int(input())

a = [None] * (N + 1)
a[1] = 1
a[2] = 1
for i in range(2, N):
    a[i + 1] = (a[i - 1] + a[i]) % 1000000007

print(a[N])
