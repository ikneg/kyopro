n = int(input())

points = [ list(map(int, input().split())) for _ in range(n)]

ans = 0
y_min = 1000000000000000000000000000000000000000000
points.sort()
for i in range(n):
    if points[i][1] < y_min:
        ans += 1
        
    y_min = min(points[i][1], y_min)
print(ans)