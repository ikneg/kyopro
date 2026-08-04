s = list(input())
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = list()

for letter in s:
    for num in numbers:
        if letter == str(num):
            answer.append(str(num))
print("".join(answer))
