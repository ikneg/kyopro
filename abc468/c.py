import itertools

n = int(input())
#順列全探索やりましょう

p = list(map(int, input().split()))
q = list(map(int, input().split()))

all_p = itertools.permutations([ i for i in range(1, n+1)])
ans = 0

for item in all_p:
    if p < list(item) < q:
        ans += 1
print(ans)