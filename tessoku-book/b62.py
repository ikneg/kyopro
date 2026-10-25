from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    used[start] = True

    while que:
        pos = que.popleft()

        for nxt in G[pos]:
            if not used[nxt]:
                root[nxt] = pos
                used[nxt] = True
                que.append(nxt)


N, M = map(int, input().split())
G = [[] for _ in range(N)]
root = [[] for _ in range(N)]
root[0] = [0]
used = [False] * N

for i in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    G[A].append(B)
    G[B].append(A)

bfs(0)
ans = [N]
idx = N-1
while idx != 0:
    idx = root[idx]
    ans.append(idx+1)

print(*reversed(ans))