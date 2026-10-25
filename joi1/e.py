import sys
S = input()
addChar = ["JOIG", "JOI", "IOI"]
length = [4, 3, 3]
sys.setrecursionlimit(10 ** 6)
ok = True
def dfs(l):
    if l >= len(S):
        return True
    for i, item in enumerate(addChar):
        if S[l:l+length[i]] == item:
            l += length[i]
            dfs(l)
            break
    else:
        print("No")
        sys.exit()

dfs(0)
print("Yes")




