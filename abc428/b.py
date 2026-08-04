n, k = map(int, input().split())
s = list(input())
words = {}

for i in range(n-k+1):
    if ''.join(s[i:i+k]) in words:
        words[''.join(s[i:i+k])] += 1
    else:
        words[''.join(s[i:i+k])] = 1


max_value = max(words.values())
print(max_value)
ans = []

for key in words:
    if words[key] == max_value:
        ans.append(key)

ans.sort()
print(*ans)
