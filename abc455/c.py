n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a_temp = [0] * n

a_temp_index = 0
for i in range(n):
    if i == 0:
        a_temp[a_temp_index] += a[i]
        continue
    else:
        if a[i] == a[i-1]:
            a_temp[a_temp_index] += a[i]
        else:
            a_temp_index += 1
            a_temp[a_temp_index] += a[i]

a_temp.sort(reverse=True)

for i in range(k):
    a_temp[i] = 0

print(sum(a_temp))