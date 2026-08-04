n = int(input())
s = list(input())

atari = []
fall = []
atari_temp = 0
fall_temp = 0

for i in range(n):
    if s[i] == "o":
        atari_temp += 1
    else:
        fall_temp += 1
    fall.append(fall_temp)
    atari.append(atari_temp)

L = 0
for i in range(n):
    life = atari[i] + fall[i]
    while life - fall[L] > 0 and L != n-1:
        L += 1
    print(L+1)
        