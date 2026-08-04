h, w, n = map(int, input().split())
a = []

for _ in range(h):
    a_i = list(map(int, input().split()))
    a.append(a_i)

host_scream = [int(input()) for _ in range(n)]

ans = []

for i in range(h):
    count = 0
    for integer in a[i]:
        for scream_integer in host_scream:
            if integer == scream_integer:
                count += 1
    ans.append(count)

print(max(ans))