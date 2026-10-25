from sortedcontainers import SortedList
Q,V=map(int,input().split())
battery=SortedList()

for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        _,t,w=query
        battery.add(w-t)
    else:
        _,t=query
        if not battery:
            print(-1)
        else:
            x=battery.pop(-1)
            print(min(x+t,V))

