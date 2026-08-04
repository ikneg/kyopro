n = int(input())
t = list(map(int, input().split()))

rank = sorted(enumerate(t, start=1), key=lambda x: x[1])
print(rank[0][0], rank[1][0], rank[2][0])