import math

def divisor(num):
    temp = []
    for dividend in range(1, int(math.sqrt(num)) + 1):
        if num % dividend == 0:
            temp.append(dividend)
            if num / dividend != dividend:
                temp.append(num // dividend)

    return temp

n = int(input())
a = list(map(int, input().split()))

ans = 0
cumulative = [0]
temp_sum = 0

for i in range(n):
    temp_sum += a[i]
    cumulative.append(temp_sum)

for l in range(n):
    for r in range(l+1, n):
        check_sum = cumulative[r+1] - cumulative[l]
        unbreakable = True
        divisors = divisor(check_sum)

        for i in range(l, r+1):
            if a[i] in divisors:
                unbreakable = False
                break

        if unbreakable:
            ans += 1

print(ans)



