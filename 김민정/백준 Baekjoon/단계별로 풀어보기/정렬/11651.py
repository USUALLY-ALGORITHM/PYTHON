# 좌표 정렬하기 2 (https://www.acmicpc.net/problem/11651)

N = int(input())
array = []

for _ in range(N):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(array[i][0], array[i][1])