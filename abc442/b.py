import sys

input = sys.stdin.readline

LOWERCASE = list("abcdefghijklmnopqrstuvwxyz")
UPPERCASE = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

q = int(input())

playing = False
volume = 0

for i in range(q):
    a = int(input())

    if a == 1:
        volume += 1
    elif a == 2:
        if volume >= 1:
            volume -= 1
    else:
        if playing:
            playing = False
        else:
            playing = True

    if playing and volume >= 3:
        print('Yes')
    else:
        print('No')