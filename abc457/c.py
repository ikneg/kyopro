n, k = map(int, input().split())

words = [0] * n

for i in range(n):
    l, *a = map(int, input().split())
    
    words[i] = [l, a]

c = list(map(int, input().split()))

count = 0

for i in range(n):

    if count + words[i][0] * c[i] < k:
        count += words[i][0] * c[i]
    else:
        if (k - count) % words[i][0] == 0:
            print(words[i][1][words[i][0]-1])
        else:
            print(words[i][1][((k - count) % words[i][0]) - 1])
        break