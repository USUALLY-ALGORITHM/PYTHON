# 동전 0 (https://www.acmicpc.net/problem/11047)

N, K = map(int, input().split())
coin = []

for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)

count = 0
for i in range(N):
    count += K // coin[i]
    K = K % coin[i]
print(count)