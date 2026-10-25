N,M=map(int,input().split())
S=[input() for _ in range(N)]
T=[input() for _ in range(M)]
ans=[0]*N
for j in range(M):
    if T[j] in S:
        ans[S.index(T[j])] += 1

    else:
        I=[]
        for i in range(N):
            if len(S[i])==len(T[j]) and sum(s!=t for s,t in zip(S[i],T[j]))==1:
                I.append(1)

        if len(I)==1:
            ans[I[0]]+=1

print(*ans,sep="\n")
    
    