n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

room = [0] * (n)

for i in range(n-1):
    if i == 0:
        use_a = a[i]
        room[i+1] = use_a
    else:
        use_a = room[i] + a[i]
        use_b = room[i-1] + b[i-1]
        room[i+1] = min(use_a, use_b)
print(room[n-1])
