# tupleを使おう!

m, d = map(int, input().split())
festival = {(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)}

if (m, d) in festival:
    print("Yes")
else:
    print("No")
