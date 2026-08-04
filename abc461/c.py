n, k, m = map(int, input().split())

jewelry = []
kind = set()
for i in range(n):
    c, v = map(int, input().split())
    jewelry.append([v, c])

jewelry = sorted(jewelry, reverse=True)

value = 0
L = 0
for i in range(k):
    if m - len(kind) == k-i:
        while jewelry[i+L][1] in kind:
            L += 1
    value += jewelry[i+L][0]
    kind.add(jewelry[i+L][1])
print(value)