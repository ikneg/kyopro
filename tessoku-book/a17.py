n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

room = [0] * n
room_step = [0] * n

for i in range(n-1):
    if i == 0:
        use_a = a[i]
        room[i+1] = use_a
        room_step[i+1] = 1
    else:
        use_a = room[i] + a[i]
        use_b = room[i-1] + b[i-1]

        if use_a <= use_b:
            room_step[i+1] = i+1
            room[i+1] = use_a
        else:
            room_step[i+1] = i
            room[i+1] = use_b

        # room[i+1] = min(use_a, use_b)


def restoration(index):
    temp = []
    temp.append(index)
    count = index
    while True:
        count = room_step[count-1]
        if count == 0:
            break
        temp.append(count)
    return temp

ans = list(reversed(restoration(n)))
print(len(ans))
print(*ans)
