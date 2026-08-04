s = list(input())
east = s.count("E")
west = s.count("W")

if east > west:
    print("East")
else:
    print("West")
