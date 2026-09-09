import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

dictionary = itertools.permutations([(i+1) for i in range(N)])

a = 0
b = 0

for idx, item in enumerate(dictionary):
    if P == item:
        a = idx
    if Q == item:
        b = idx

print(abs(a - b))