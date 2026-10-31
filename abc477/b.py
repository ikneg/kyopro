N,D=map(int,input().split())
X=[(x,i+1) for i,x in enumerate(map(int,input().split()))]
X.sort()
ans=[]
for i in range(N):
    if i==0:
        if abs(X[0][0]-X[1][0])>=D:
            ans.append(X[0][1])
    elif i==N-1:
        if abs(X[N-1][0]-X[N-2][0])>=D:
            ans.append(X[N-1][1])
    else:
        if abs(X[i][0]-X[i-1][0])>=D and abs(X[i][0]-X[i+1][0])>=D:
            ans.append(X[i][1])

if ans:
    print(len(ans))
    ans.sort()
    print(*ans)
else:
    print(0)