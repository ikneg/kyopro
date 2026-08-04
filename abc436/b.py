n = int(input())

grid = [[0] * n for _ in range(n)]

k = 1
r = 0
c = (n - 1) // 2
grid[r][c] = k

for i in range(n * n - 1):
    if grid[(r - 1) % n][(c + 1) % n] == 0:
        c = (c + 1) % n
        r = (r - 1) % n
        grid[r][c] = k + 1
    else:
        r = (r + 1) % n
        grid[r][c] = k + 1
    k += 1

for ans in grid:
    print(*ans)