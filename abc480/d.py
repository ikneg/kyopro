from bisect import bisect_left, bisect_right
N,Q=map(int, input().split())
A=list(map(int, input().split()))

S=[0]
for a in A: S.append(S[-1]+a)
T=[(0,0)]
for i,s in enumerate(S[1:], 1):
    ti,tt=T[-1]
    T.append((ti+i, tt+s))

def f(x):
    i=bisect_right(T,(x,100**18))-1
    ti,tt=T[i]
    return tt+S[x-ti]

for _ in range(Q):
    L,R=map(int,input().split())
    print(f(R)-f(L-1))



