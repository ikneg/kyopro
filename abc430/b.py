n, m = map(int, input().split())

s = [0] * n
solve = [0] * (n - m + 1) ** 2
for i in range(n):
    s[i] = list(input())

cut_count = 0
for i in range(n - m + 1):
    for j in range(n - m + 1):
        temp = [0] * m * m
        count = 0
        for height in range(m):
            for width in range(m):
                temp[count] = s[i+height][j+width]
                count += 1
        solve[cut_count] = temp
        cut_count += 1
print(len(set(map(tuple, solve))))
