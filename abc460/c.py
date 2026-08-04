n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

L = 0
ans = 0
enddayo = False
for i in range(n):
    if a[i] * 2 >= b[L]:
        ans += 1
        L += 1
        if L == m:
            break

        
print(ans)