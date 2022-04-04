# 분해합 (https://www.acmicpc.net/problem/2231)

N = int(input())

for i in range(1, N + 1):
    num = sum(map(int, str(i)))
    num_sum = i + num # i = 245, num = 2 + 4 + 5

    if num_sum == N:
        print(i)
        break
    if i == N:
        print(0)