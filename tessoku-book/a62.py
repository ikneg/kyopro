from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    used[start] = True

    while que:
        pos = que.popleft()

        for nxt in G[pos]:
            if not used[nxt]:
                used[nxt] = True
                que.append(nxt)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
used = [False] * N

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    G[A].append(B)
    G[B].append(A)

bfs(0)
for i in used:
    if not i:
        print("The graph is not connected.")
        break
else:
    print("The graph is connected.")

    

