S = input()
S1 = input()
S = S + S1[:]

Aidx = S.index("A")

if Aidx % 2 == 0:
    if S[Aidx - 2] == "D" or S[Aidx + 1] == "D":
        print("Yes")
    else:
        print("No")
else:
    if S[Aidx - 2] == "D" or S[Aidx-1] == "D":
        print("Yes")
    else:
        print("No")