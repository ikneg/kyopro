from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    used[start] = True

    while que:
        pos = que.popleft()

        for nxt in G[pos]:
            if not used[nxt]:
                dist[nxt] = dist[pos] + 1
                used[nxt] = True
                que.append(nxt)

N, M = map(int, input().split())
dist = [-1] * N
dist[0] = 0
used = [False] * N
G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    G[A].append(B)
    G[B].append(A)

bfs(0)
for ans in dist:
    print(ans)