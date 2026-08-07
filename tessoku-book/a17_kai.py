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

def restoration():
    temp = [n]
    count = n-1
    b.insert(0, 0)
    while count > 0:
        a_way = room[count - 1] + a[count - 1]
        b_way = room[count - 2] + b[count - 1]
        if a_way == room[count]:
            count -= 1
            temp.append(count+1)
        else:
            count -= 2
            temp.append(count+1)

    return list(reversed(temp))

ans = restoration()

print(len(ans))
print(*ans)
