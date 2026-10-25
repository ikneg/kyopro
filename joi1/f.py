N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [[A[i], i] for i in range(N)]
B = [[B[i], i] for i in range(N)]
A.sort(reverse=True)
B.sort(reverse=True)
used = set()
AL = 0
BL = 0
Ai = 0
Bi = 0

ans = 0
for i in range(N):
    if A[AL][0] > B[BL][0] and Bi >= Y and Ai < X:
        Ai += 1
        ans += A[AL][0]
        used.add(A[AL][1])
        AL += 1
    else:
        Bi += 1
        ans += B[BL][0]
        used.add(B[BL][1])
        BL += 1

    while A[AL][1] in used:
        AL += 1

    while B[BL][1] in used:
        BL += 1
print(ans)
