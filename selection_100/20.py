import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for b in B:
    canA = bisect.bisect_left(A, b)
    canC = N - bisect.bisect_right(C, b)
    ans += canA * canC


print(ans)
