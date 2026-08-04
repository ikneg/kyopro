n, m = map(int, input().split())
a = list(map(int, input().split()))
temp = []
for i in range(1,n+1):
    temp = a[:i-1] + a[i:]
    if sum(temp) == m:
        print('Yes')
        break
else:
    print('No')
