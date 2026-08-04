n, m = map(int, input().split())
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = input()
t = input()
count = [0] * (n-m+1)
for i in range(n-m+1):
    for j in range(m):
        count[i] += min(
            10 + int(s[i+j]) - int(t[j]),
            abs(int(s[i+j]) - int(t[j]))
            if int(s[i+j]) >= int(t[j])
            else 10
        )
print(min(count))