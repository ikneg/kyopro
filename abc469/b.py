n = int(input())

s_input = list(input())

s = ["x"]
for i in s_input:
    s.append(i)
s.append("x")
ans = 0
for i in range(n):
    center = i+1
    if s[center] == s[center-1] == s[center+1] == "x":
        ans += 1
print(ans)