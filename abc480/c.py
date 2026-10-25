from collections import deque
def ceil(a, b):
    return (a + b - 1) // b

N, K, T = map(int, input().split())
A = [T]
for i in map(int, input().split()):
    A.append(i)

A.sort()
R = 0
N = len(A)
for i in range(N):
    if A[i] > T:
        A[i] = T
ans = 0


for i in range(N):
    if i == 0:
        R = A[i] + K
        ans += ceil(A[i], K)

    elif i < N:
        if R > A[i]:
            R = A[i] + K
        else:
            ans += ceil(A[i] - R, K)
            R = A[i] + K

print(ans)
