import math

n = int(input())

count = n
ans = []

for i in range(2, int(math.sqrt(n))+1):
    while count % i == 0 and not count == 1:
        ans.append(i)
        count //= i 

if count != 1:
    ans.append(count)

print(*ans)