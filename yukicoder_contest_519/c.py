N,K=map(int,input().split())
P=list(map(int,input().split()))
Pa = sorted(P)

ans=[]

for i in range(N-K):
    j=i+K
    if P[i]==Pa[j] and P[j]==Pa[i]:
        ans.append((i+1,j+1))

for a, b in ans:
    a,b=a-1,b-1
    P[a],P[b]=P[b],P[a]

for i in range(N):
    if P[i]!=Pa[i]:
        a,b=i,P[i]-1
        if a < b:
            ans.append((a+1,b+1))
        else:
            ans.append((b+1,a+1))

        P[a],P[b]=P[b],P[a]


print(len(ans))
for a,b in ans:
    print(a,b)

print(P)

