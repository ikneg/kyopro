n = int(input())
s = list(input())
count = 0

for l in s:
    if l != "o":
        break

    count += 1

print("".join(s[count:]))
