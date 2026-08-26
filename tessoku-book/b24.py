import bisect

N = int(input())
boxes = [[0] * 2 for _ in range(N)]

for i in range(N):
    x, y = map(int, input().split())
    boxes[i][0] = x
    boxes[i][1] = -y

boxes.sort()

X = [ None ] * N
Y = [ None ] * N

for i in range(N):
    X[i] = boxes[i][0]
    Y[i] = -boxes[i][1]


LEN = 0
L = []

for i in range(N):
    pos = bisect.bisect_left(L, Y[i])

    if pos == LEN:
        LEN += 1
        L.append(Y[i])
    else:
        L[pos] = Y[i]

print(LEN)
