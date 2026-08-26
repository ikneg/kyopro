A, B = map(int, input().split())
save_A = A
save_B = B

while not A == 0 and not B == 0:
    if A > B:
        A = A % B
    else:
        B = B % A

gcd = max(A, B)

print((save_A * save_B) // gcd)