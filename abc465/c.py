n_len = int(input())
n = [0] * n_len * 2
s = list(input())
direction = 1
l = 0
r = 0

for i in range(n_len):
    if direction == -1:
        l += 1
        n[n_len - l] = i+1
    else:
        n[n_len + r] = i+1
        r += 1
    if s[i] == "o" and i > 0:
        direction *= -1
print(*[x for x in n[::direction] if x != 0])