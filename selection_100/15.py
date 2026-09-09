import math, itertools
N = int(input())
cities = [[] for _ in range(N)]

for i in range(N):
    cities[i] = list(map(int, input().split()))

l = [(i+1) for i in range(N)]

p = itertools.permutations(l)

ans = 0
for i in p:
    for j in range(N-1):
        ans += math.dist(cities[i[j]-1], cities[i[j+1]-1])

print(ans / math.factorial(N))