# 블랙잭 (https://www.acmicpc.net/problem/2798)

N, M = map(int, input().split())
card = list(map(int, input().split()))

sum = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                sum = max(sum, card[i] + card[j] + card[k])
print(sum)