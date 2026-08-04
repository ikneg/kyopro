n = input()

happy_temp = []
ans = 'Yes'

while n != "1":
    n = sum([ int(i) ** 2 for i in n])
    n = str(n)
    if n in happy_temp:
        ans = 'No'
        break
    happy_temp.append(n)
print(ans)