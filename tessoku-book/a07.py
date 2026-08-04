d = int(input())
n = int(input())
number_participants = [0] * (d+1)

for i in range(n):
    l, r = map(int, input().split())
    number_participants[l-1] += 1
    number_participants[r] -= 1

for i in range(0, d):
    number_participants[i+1] += number_participants[i]
    print(number_participants[i])