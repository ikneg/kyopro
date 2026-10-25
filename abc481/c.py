Q=int(input())
data={}
searchdata=set()
R=1
for i in range(Q):
    S=input()
    if S not in searchdata:
        searchdata.add(S)
        data[S]=R
        print(R)
        R+=1
    else:
        print(data[S])
