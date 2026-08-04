n = int(input())

a = [[0] * n for i in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1, n):
        if 1 != 0 and a[i-1][j] == "Yes":
            a[i][j] = "Yes"
            ans += 1
            continue

        if a[i][j-1] == "Yes" or j - i == 1:
            print("?", i+1, j+1, flush=True)
            temp = input()
            if temp == "Yes":
                ans += 1
            a[i][j] = temp
        else:
            a[i][j] = "No"
print("!", ans, flush=True)
