import math

def divisors(num):
    temp = [0] * num
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            temp[i-1] = 1
            if num // i != i:
                temp[(num // i)-1] = 1

    return temp

a, b = map(int, input().split())

divisor = divisors(100)

for i in range(a, b+1):
    if divisor[i-1] == 1:
        print("Yes")
        break
else:
    print("No")