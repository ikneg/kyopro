N, H, W = map(int, input().split())
A = [0] * N
B = [0] * N

nimu = []

for i in range(N):
    A[i], B[i] = map(int, input().split())

nimu_sum = 0
for i in range(N):
    nimu_sum = (nimu_sum ^ (A[i] - 1))
    nimu_sum = (nimu_sum ^ (B[i] - 1))

if nimu_sum != 0:
    print("First")
else:
    print("Second")