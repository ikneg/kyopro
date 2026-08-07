n = int(input())
h = list(map(int, input().split()))

#ズレを考慮しよう
dp = [0] * n
for i in range(n-1):
    if i == 0:
        step = abs(h[i+1] - h[i])
        dp[i+1] = step
    else:
        step = dp[i] + abs(h[i+1] - h[i])
        skip = dp[i-1] + abs(h[i+1] - h[i-1])
        dp[i+1] = min(step, skip)

def restoration():
    temp = [n]
    loop = n-1
    while loop > 0:
        if loop == 1:
            loop -= 1
            temp.append(loop+1)
        else:
            step = abs(h[loop] - h[loop-1]) + dp[loop-1]
            skip = abs(h[loop] - h[loop-2]) + dp[loop-2]
            if step < skip:
                loop -= 1
                temp.append(loop+1)
            else:
                loop -= 2
                temp.append(loop+1)


    return list(reversed(temp))
ans = restoration()
print(len(ans))
print(*ans)
