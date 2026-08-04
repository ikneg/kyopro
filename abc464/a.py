s = list(input())
east = 0
west = 0

for army in s:
    if army == "E":
        east += 1
    else:
        west += 1
if east > west:
    print("East")
else:
    print("West")
