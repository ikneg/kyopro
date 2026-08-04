n, q = map(int, input().split())

offset = 0
answer = [0] * q
blocks = [0] * n

for i in range(q):
    kind, value = map(int, input().split())

    if kind == 1:
        x = value - 1

        blocks[x] += 1
        answer[blocks[x] - 1] += 1

        if answer[offset] == n:
            offset += 1
    else:
        index = value - 1 + offset
        if index < q:
            print(answer[value-1+offset])
        else:
            print(0)