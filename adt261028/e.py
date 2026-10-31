N=int(input())
A=list(map(int,input().split()))
A.sort()
maxL=0
twoL=max(A)
if N%2==0:
    maxL=(A[N//2]+A[N//2-1])
else:
    maxL=(A[0]+A[-1])

ans=[]
cnt=A.count(twoL)
if N%2==0:
    for i in range(N//2):
        if not(A[i] + A[-i-1] == maxL):
            break
    else:
        ans.append(maxL)

if N != cnt:
    if (N-cnt)%2==0:
        for i in range(N//2):
            if not(A[i] + A[-i-1-cnt] == twoL):
                break
        else:
            ans.append(twoL)
else:
    ans.append(twoL)



print(*sorted(ans))