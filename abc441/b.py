n, m = map(int, input().split())

s = list(input())
t = list(input())
q = int(input())

#niziuループ
#s takahashi go
#t aoki go

for i in range(q):
    w = input()
    found_or = "Unknown"

    for letter in w:

        if letter in s and not letter in t:
            found_or = "Takahashi"
            break

        elif letter in t and not letter in s:
            found_or = "Aoki"
            break

    print(found_or)

