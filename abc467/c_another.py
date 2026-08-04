n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

first_zero = [0]
first_one = [1]
count_zero = 0
count_one = 1

for i in range(n-1):
    first_zero.append(abs(first_zero[i] - b[i]))
    first_one.append(abs(first_one[i] - b[i]))
    if first_zero[i+1] != a[i+1]:
        count_zero += 1
    if first_one[i+1] != a[i+1]:
        count_one += 1

print(min(count_one, count_zero))
