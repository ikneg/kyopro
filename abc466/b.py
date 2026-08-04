n, m = map(int, input().split())

balls = {}

answer = []

for i in range(n):
    c, s = map(int, input().split())
    if c not in balls or s > balls[c]:
        balls[c] = s
for i in range(1, m + 1):
    if i in balls:
        answer.append(balls[i])
    else:
        answer.append(-1)
print(*answer)
