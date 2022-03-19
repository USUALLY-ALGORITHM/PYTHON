# 회의실 배정 (https://www.acmicpc.net/problem/1931)

N = int(input())

array = []
for _ in range(N):
    start, end = map(int, input().split())
    array.append((start, end))

array = sorted(array, key=lambda x: x[0])
array = sorted(array, key=lambda x: x[1])

count, start_time = 0, 0
for i in range(N):
    if array[i][0] >= start_time:
        start_time = array[i][1]
        count += 1

print(count)



