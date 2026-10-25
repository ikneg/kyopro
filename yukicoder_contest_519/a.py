N,A,B=map(int,input().split())

ans = 0
for i in range(1, N+1):
    if i % A > i % B:
        ans += 1
print(ans)