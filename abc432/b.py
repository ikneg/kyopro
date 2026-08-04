x = list(input())
zero_count = 0

number_temp = []
for i in x:
    if i == '0':
        zero_count += 1
    else:
        number_temp.append(i)

number_temp.sort()

for i in range(zero_count):
    number_temp.insert(1, '0')

print(''.join(number_temp))
