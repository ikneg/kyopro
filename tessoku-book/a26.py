import math

def check_prime_number(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return 'No'
    else:
        return 'Yes'
        

Q = int(input())

for _ in range(Q):
    temp = int(input())
    print(check_prime_number(temp))