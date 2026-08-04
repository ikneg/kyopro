import sys

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k:
                break
            if a[i] + a[j] + a[k] == 1000:
                print("Yes")
                sys.exit()
else:
    print("No")