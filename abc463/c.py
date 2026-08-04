from bisect import bisect_right

n = int(input())

height = []
leave_time = []

for i in range(n):
    h, l = map(int, input().split())
    height.append(h)
    leave_time.append(l)

query = int(input())
t = list(map(int, input().split()))

max_value = [0] * n
temp = 0

for q in range(n-1,-1,-1):
    temp = max(height[q], temp)
    max_value[q] = temp

for awewewe in t:
    index = bisect_right(leave_time, awewewe)
    print(max_value[index])
    
# index = bisect_right(leave_time, awewewe) <- 
#for time in t:
#   print(max_value[time-1])
        