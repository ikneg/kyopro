N,L=map(int,input().split())
ans=0
for _ in range(N):
    a,b=input().split()
    a=int(a)
    if b=="E":
        if L-a>ans:
            ans=L-a
    else:
        if a>ans:
            ans=a

print(ans)