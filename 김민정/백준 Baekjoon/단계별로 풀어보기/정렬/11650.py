# 좌표 정렬하기 (https://www.acmicpc.net/problem/11650)

N = int(input())
array = []

for _ in range(N):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort()

for i in range(N):
    print(array[i][0], array[i][1])