def power(a, b, m):
    p = a
    Answer = 1
    for i in range(65):
        wari = 2**i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m

        p = (p * p) % m

    return Answer


a, b = map(int, input().split())

print(power(a, b, 1000000007))
