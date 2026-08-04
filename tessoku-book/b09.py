n = int(input())
grid_size = 1509

grid = [[0] * grid_size for _ in range(grid_size)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[a][d] -= 1
    grid[c][b] -= 1
    grid[c][d] += 1

for i in range(0,grid_size):
    for j in range(1,grid_size):
        grid[i][j] = grid[i][j] + grid[i][j-1]

for j in range(0,grid_size):
    for i in range(1,grid_size):
        grid[i][j] = grid[i][j] + grid[i-1][j]

for j in range(0,grid_size):
    for i in range(0,grid_size):
        if grid[i][j] > 1:
            grid[i][j] = 1

ans = 0
for i in range(grid_size):
    ans += sum(grid[i])
print(ans)