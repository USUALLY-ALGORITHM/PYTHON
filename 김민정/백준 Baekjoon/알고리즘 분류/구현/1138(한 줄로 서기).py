# 한 줄로 서기 (https://www.acmicpc.net/problem/1138)

N = int(input())
H = list(map(int, input().split()))

result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == H[i] and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

for i in result:
    print(i, end=" ")