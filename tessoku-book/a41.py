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
S=input()
cnt=0
before=""
for x in S:
    if before!="" and before!=x:
        cnt=1
    else:
        cnt+=1
    
    if cnt==3:
        print("Yes")
        sys.exit()

    before=x
    
print("No")