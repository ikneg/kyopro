s = input()

ans = 0
l = 0
for i in range(len(s)-1):
    l = max(l, i)
    if l != len(s)-1:
        while s[l] != s[l+1]:
            l += 1
            if l == len(s)-1:
                break
    
    ans += l - i
    
ans += len(s)

print(ans % 998244353)