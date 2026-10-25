#ブルーアーカイブ！！！！！！！！！！おわああああああ！！！！！

import math
from collections import deque
from heapq import heappush, heappop

def zero_one_bfs(G, S):
    N = len(G)
    dist = [float('inf')] * N
    dist[S] = 0

    q = deque([(0, S)])


    while q:
        cost, v = q.popleft()

        if cost > dist[v]:
            continue

        for nv, w in G[v]:
            nc = cost + w

            if nc < dist[nv]:
                dist[nv] = nc
                if w == 1:
                    q.append((nc, nv))
                else:
                    q.appendleft((nc, nv))

    return dist

N,M,S,T=map(int,input().split())
G=[[] for _ in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    G[a].append((b, 1))

for i in range(N):
    if G[i]:
        minNode = min(v for v, w in G[i])
        for j in range(len(G[i])):
            v, w = G[i][j]
            if v==minNode:
                G[i][j]=(v,0)
                break

dist=zero_one_bfs(G, S-1)
if dist[T-1]==float('inf'):
    print(-1)
else:
    print(dist[T-1])


