n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

total = set()

for bit in range(1 << n):
    res = 0
    for i in range(n):
        if bit & (1 << i):
            res += A[i]

    total.add(res)

for target in m:
    if target in total:
        print("yes")
    else:
        print("no")
