h, w, n = map(int, input().split())

snowfall = [[0] * (w + 1) for _ in range(h + 1)]

for _ in range(n):
    a, b, c, d = map(int, input().split())

    snowfall[a - 1][b - 1] += 1
    snowfall[c][b - 1] -= 1
    snowfall[a - 1][d] -= 1
    snowfall[c][d] += 1

for i in range(h):
    for j in range(1, w):
        snowfall[i][j] += snowfall[i][j - 1]

for i in range(1, h):
    for j in range(w):
        snowfall[i][j] += snowfall[i - 1][j]

for i in range(h):
    print(*snowfall[i][:w])