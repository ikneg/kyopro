n = int(input())
a = list(map(int, input().split()))
q = int(input())

atari_sum = [0] * (n + 1)
hazure_sum = [0] * (n + 1)

for i in range(1, n+1):
    if a[i-1] == 1:
        atari_sum[i] = atari_sum[i-1] + 1
        hazure_sum[i] = hazure_sum[i-1]
    else:
        atari_sum[i] = atari_sum[i-1]
        hazure_sum[i] = hazure_sum[i-1] + 1

for i in range(q):
    l, r = map(int, input().split())
    if hazure_sum[r] - hazure_sum[l-1] > atari_sum[r] - atari_sum[l-1]:
        print("lose")
    elif hazure_sum[r] - hazure_sum[l-1] < atari_sum[r] - atari_sum[l-1]:
        print('win')
    else:
        print('draw')
    