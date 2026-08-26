N = int(input())

A = list(map(int, input().split()))

xor_sum = 0

for item in A:
    xor_sum = xor_sum ^ item

if xor_sum != 0:
    print("First")
else:
    print("Second")