S=input()
N=len(S)
L,R=0,0
C=0
if N%2==0:
    L=N//2-1
    R=N//2
else:
    L=N//2-1
    R=N//2+1

for i in range(L+1):
    if S[L-i]!=S[R+i]:
        C+=1
print(C)