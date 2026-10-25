A = list(map(int, input().split()))
win = [[0] * 2 ** i for i in range(6)]
win[5] = A

for i in range(5, -1, -1):
    for j in range(0, 2 ** i - 1, 2):
        if win[i][j] > win[i][j+1]:
            win[i-1][j//2] = win[i][j]
        else:
            win[i-1][j//2] = win[i][j+1]


if win[1][0] == win[0][0]:
    print(A.index(win[1][1])+1)
else:
    print(A.index(win[1][0])+1)