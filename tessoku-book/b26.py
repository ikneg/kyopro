import math

N = int(input())

deleted = [True] * N
deleted[0] = False

for i in range(2, int(math.sqrt(N)) + 1):
    count = 2
    while count * i <= N:
        deleted[(count * i) - 1] = False
        count += 1

for i in range(N):
    if deleted[i] == True:
        print(i+1)