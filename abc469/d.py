n, m = map(int, input().split())

success = [1, 1, 1, 1]

pattern = []



temp_a = 0
temp_b = 0
for i in range(m):
    a, b = map(int, input().split())
    if i == 0:
        if m == 1:
            success = [1]
        else:
            temp_a = a
            temp_b = b
            continue
    if i == 1:
        pattern = [[temp_a, a], [temp_a, b], [temp_b, a], [temp_b, b]]

        for i in range(4):
            if pattern[i][0] == pattern[i][1]:
                success[i] = 0
            for j in range(4):
                if pattern[i] in pattern[j]:
                    success[i] = 0

    else:
        for index, item in enumerate(pattern):
            if not a in item and not b in item:
                success[index] = 0
print(sum(success))