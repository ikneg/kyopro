n, m = map(int, input().split())

birdDatas = []
birds = [0] * (n+1)
L = 0

for i in range(n):
    a, d, b = map(int, input().split())
    birds[a] += 1
    birdDatas.append([d, a, b])

birdDatas.append([5000000000, 1, 1])

kind = sum(count > 0 for count in birds)

birdDatas.sort(key=lambda x: x[0])

for day in range(1, m + 1):
    while birdDatas[L][0] == day:
        before = birdDatas[L][1] 
        after = birdDatas[L][2] 

        birds[before] -= 1
        if birds[before] == 0:
            kind -= 1

        birds[after] += 1
        if birds[after] == 1:
            kind += 1
            
        L += 1
    print(kind)
