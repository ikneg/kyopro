def power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2**i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m

        p = (p * p) % m

    return Answer


def Division(a, b, m):
    return (a * power(b, m - 2, m)) % m


n, r = map(int, input().split())

permutation = [0] * 100001
permutation[0] = 1

for i in range(1, 100001):
    permutation[i] = (permutation[i - 1] * i) % 1000000007

molecule = permutation[n]

denominator = permutation[r] * permutation[n - r]

print(Division(molecule, denominator, 1000000007))
