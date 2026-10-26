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

N=int(input())
grid=[list(map(int, input().split())) for _ in range(N)] 
Q=int(input())
T=[i for i in range(N)]
for i in range(Q):
    q=list(map(int, input().split()))
    if q[0]==1:
        _,x,y=q
        x,y=x-1,y-1
        T[x],T[y]=T[y],T[x]
    else:
        _,x,y=q
        print(grid[T[x-1]][y-1])
    