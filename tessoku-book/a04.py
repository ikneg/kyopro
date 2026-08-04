n = list(input())
ans = 0
digits_number = len(n)

for i in range(digits_number):
    if n[i] == "1":
        ans += 1 * (2 ** (digits_number -1))
print()