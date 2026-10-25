N = int(input())
HS = [tuple(map(int, input().split())) for _ in range(N)]

deadlines = [0] * N

def ok(x):

    for i in range(N):
        h, s = HS[i]
        if x < h:
            return False
        deadlines[i] = (x - h) // s

    deadlines.sort()

    for i in range(N):
        if deadlines[i] < i:
            return False

    return True

left = 0
right = 10 ** 18

while right - left > 1:
    mid = (left + right) // 2

    if ok(mid):
        right = mid
    else:
        left = mid

print(right)