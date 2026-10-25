from collections import defaultdict
H, W = map(int, input().split())
grid = [[] for _ in range(H)]
move = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

for i in range(H):
    grid[i] = list(input().split())


baba = set()
N = int(input())
temp = [[] for _ in range(N)]

for i in range(N):
    temp[i] = list(input().split())
    baba.add(temp[i][0])
    baba.add(temp[i][1])

baba = sorted(list(baba))

bababa = defaultdict()
    
G = [[] for i in range(len(baba))]

for i in range(len(baba)):
    bababa[baba[i]] = i

for i in range(N):
    G[baba.index(temp[i][0])].append(temp[i][1])

for i in range(H):
    for j in range(W):
        for be in range(len(baba)):
            if grid[i][j] == baba[be] and len(G[be]) > 0:
                for dy, dx in move:
                    cy = i + dy
                    cx = j + dx
                    if 0 <= cx < W and 0 <= cy < H:
                        if grid[cy][cx] in G[be]:
                            grid[cy][cx] = "-"

for i in range(H):
    print(*grid[i])