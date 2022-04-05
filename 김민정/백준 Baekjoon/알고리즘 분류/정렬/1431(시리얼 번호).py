# 시리얼 번호 (https://www.acmicpc.net/problem/1431)

N = int(input())
array = []

for _ in range(N):
    s = input()
    num = 0

    for i in s:
        if i.isdigit():
            num += int(i)
    array.append([s, num])
array.sort(key=lambda x:(len(x[0]), x[1], x[0]))

for i in range(N):
    print(array[i][0])