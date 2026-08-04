n, a, b, x = map(int, input().split())

ans = (x // (a + b)) * a * n

spare_time = x % (a + b)

ans += n * min(spare_time, a)

print(ans)
