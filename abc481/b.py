#ブルーアーカイブ！！！！！！！！！！おわああああああ！！！！！
#はい。全然通らないじゃん！！！！！チキショウ！！！！いあああああああ！
#ていうかここに児童ポルノ的なこと書いたらbanされるのかな（例:イブキの____が____で___が<-付属語だけ残しておけば許されると思っていそう<-図星やめて限界)


N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=0
back=10**18
for x in A:
    if back==10**18:
        if x==K:
            ans+=1
        back=x
        continue
    if back<K and x>=K:
        ans+=1
    elif back>K and x<=K:
        ans+=1
    back=x

print(ans)