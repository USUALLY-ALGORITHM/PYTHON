# 소수 구하기 (https://www.acmicpc.net/problem/1929)

M, N = map(int, input().split())

for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1): # 제곱근까지
        if i % j == 0:
            break
    else:
        print(i)