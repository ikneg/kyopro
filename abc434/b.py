n, m = map(int, input().split())
birds = [[0] * 2 for i in range(m)]

for i in range(n):
    a, b = map(int, input().split())
    birds[a-1][0] += b
    birds[a-1][1] += 1

for i in range(m):
    print(birds[i][0] / birds[i][1])