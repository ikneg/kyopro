# ------------------------------------------------
#   _ _
#  (_) |
#   _| | ___ __   ___  __ _
#  | | |/ / '_ \ / _ \/ _` |
#  | |   <| | | |  __/ (_| |
#  |_|_|\_\_| |_|\___|\__, |
#                      __/ |
#                     |___|
# source by https://github.com/ikneg/ikneg_lib
# 15yo
# 日々飯、mono、シメジシミュレーションが好きです
# ------------------------------------------------
import sys

input = sys.stdin.readline
def I(): return input().strip()
def MS(): return input().split()
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))

abcUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abcLower = 'abcdefghijklmnopqrstuvwxyz'
# ------------------------------------------------
# ここまでがてんぷら
# ------------------------------------------------

N,M=map(int,input().split())
A=list(map(int,input().split()))
answer=[M]*N
for x in A:
    answer[x-1]-=1

print(*answer, sep="\n")