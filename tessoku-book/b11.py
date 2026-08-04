import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()

q = int(input())
for i in range(q):
    x = int(input())
    ans = bisect.bisect(a, x-1)
    print(ans)