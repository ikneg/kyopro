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


N,M=MI()
name=[I() for i in range(N)]
ans=[0]*N
for i in range(M):
    t=I()
    sameList=[]
    for i,x in enumerate(name):
        if x==t:
            ans[i]+=1
            break
        
        if len(x)==len(t) and sum(a!=b for a,b in zip(t,x))==1:
            sameList.append(i)
    else:
        if len(sameList)==1:
            ans[sameList[0]]+=1

print(*ans,sep="\n")