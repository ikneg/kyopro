a, b = map(int, input().split())

while not (a == 0 or b == 0):
    a, b = b, a%b
print(max(a, b))
