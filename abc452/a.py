m, d = map(int, input().split())

if m == 1 and d == 7:
    print("Yes")
elif m % 2 == 1 and 3 <= m <= 9 and m == d:
    print("Yes")
else:
    print("No")
