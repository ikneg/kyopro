import sys
from collections import defaultdict, deque, Counter
from itertools import accumulate, permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import gcd, lcm, isqrt, ceil, floor
import string

input = sys.stdin.readline


#ドラえもん、ぼくは緑コーダーになって富と名声を得たいです。
#しょうがないなーテッテレーgpt 6 astra


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))

def MS():
    return map(input().split())

def LSS():
    return list(input().split())


def S():
    return input().rstrip()


def ceil(a, b):
    return (a + b - 1) // b


# 文字
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
ALPHA = string.ascii_letters
DIGITS = string.digits
VOWELS = set("aeiou")

# 数値
INF = float("inf")
MOD = 998244353

# 4方向
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

# 8方向
DX8 = [1, 1, 0, -1, -1, -1, 0, 1]
DY8 = [0, 1, 1, 1, 0, -1, -1, -1]


def main():
    N, M, K = MI()
    X, Y = MI()
    A = LI()
    B = LI()
    A.sort()
    B.sort()
    Awaste = [0]
    Bwaste = [(0, 0)]

    for i in range(N):
        Awaste.append(Awaste[i] + A[i])

    for i in range(M):
        temp = (Bwaste[i][0] + ceil(B[i], K), Bwaste[i][1] + ceil(B[i], K) * K - B[i])
        Bwaste.append(temp)


    ans = 0

    for i in range(M + 1):
        cx = X
        cy = Y

        if Y < Bwaste[i][0]:
            break

        cy -= Bwaste[i][0]
        cx += Bwaste[i][1]

        money = cx + cy * K

        dessert = bisect_right(Awaste, money) - 1

        ans = max(ans, i + dessert)

    print(ans)




if __name__ == "__main__":
    main()
