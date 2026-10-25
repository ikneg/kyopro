S = input()
N = len(S)

limit = 10 ** N
isPrime = [True] * limit

if limit > 0:
    isPrime[0] = False
if limit > 1:
    isPrime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i*i, limit, i):
            isPrime[j] = False

for 

print(isPrime)