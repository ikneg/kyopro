N = int(input())
a = list(map(int, input().split()))
a = [[number, index, 0] for index, number in enumerate(a)]
a.sort()

for i in range(N):
    if i == 0:
        a[i][2] = 1
    else:
        if a[i-1][0] < a[i][0]:
            a[i][2] = a[i-1][2] + 1
        else:
            a[i][2] = a[i-1][2]

a = sorted(a, key=lambda x: x[1])

for i in range(N):
    print(a[i][2], end=" ")
print()
