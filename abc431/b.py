x = int(input())
n = int(input())
w = list(map(int, input().split()))
q = int(input())
robot_parts = [0] * n
for i in range(q):
    p = int(input())
    if robot_parts[p-1] == 0:
        robot_parts[p-1] = w[p-1]
    else:
        robot_parts[p-1] = 0

    print(sum(robot_parts) + x)
