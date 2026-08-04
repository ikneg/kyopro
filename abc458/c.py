s = list(input())

c_found = []

for index in range(len(s)):
    if s[index] == "C":
        c_found.append(index)

ans = 0

for spread in c_found:
    ans += min(spread, len(s) - 1 - spread) + 1

print(ans)