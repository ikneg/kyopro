import sys
from collections import defaultdict, deque
from math import sqrt
# import pypyjit

def ceil(a, b): return (a + b - 1) // b
def floor(a, b): return a // b
def MS(): return input().split()
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))

# pypyjit.set_param('max_unroll_recursion=-1')

abcUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abcLower = 'abcdefghijklmnopqrstuvwxyz'
sys.setrecursionlimit(10 ** 6)


H, W, K = map(int, input().split())
r = [0] * H
c = [0] * W
ans = 0
q = deque()

d = [[-1] * W for _ in range(H)]
s = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            r[i] = 1
            c[j] = 1

for i in range(H):
    for j in range(W):
        if r[i] == c[j] == 0:
            d[i][j] = 0
            q.append((i, j))


while q:
    i, j = q.popleft()
    if d[i][j] <= K:
        ans += 1
    for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if 0 <= ni < H and 0 <= nj < W:
            if s[ni][nj] == "." and d[ni][nj] == -1:
                d[ni][nj] = d[i][j] + 1
                q.append((ni, nj))


print(ans)