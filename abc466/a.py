n = int(input())
x = list(map(int, input().split()))

answer = "Yes"
for num in x:
    if num >= 0:
        answer = "No"
        break
print(answer)
