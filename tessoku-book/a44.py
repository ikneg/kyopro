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

N,Q=map(int,input().split())
ans=[i+1 for i in range(N)]
swaped=False

for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        _,x,y=query
        if swaped:  ans[-x]=y
        else:   ans[x-1]=y
    if query[0]==2:
        swaped=not swaped
    if query[0]==3:
        _,x=query
        if swaped:  print(ans[-x])
        else:   print(ans[x-1])