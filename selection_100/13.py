R, C = map(int, input().split())
osenbei = [[] for _ in range(R)]

for i in range(R):
    osenbei[i] = list(map(int, input().split()))

ans = 0
for bit in range(1 << R):
    res = 0
    for c in range(C):
        cnt = 0
        for r in range(R):
            if bit & (1 << r):
                cnt += 1 - osenbei[r][c]
            else:
                cnt += osenbei[r][c]

        res += max(cnt, R - cnt)

    ans = max(ans, res)

print(ans)
