n, m = map(int, input().split())

items = [[0] * 2] * m

for i in range(m):
    a, b = map(int, input().split())
    items[i] = [a, b]

items.sort()

kinds = [0] * n
kinds[0] = 1

for i in range(m):
    if kinds[items[i][0]-1] == 1:
        kinds[items[i][1]-1] = 1

print(sum(kinds))