n = int(input())
x = list(map(int, input().split()))

if any(n >= 0 for n in x):
    print("No")
else:
    print("Yes")
