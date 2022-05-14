# 게임을 만든 동준이 (https://www.acmicpc.net/problem/2847)

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array.reverse()
temp = array[0]
count = 0

for i in range(1, len(array)):
    while temp <= array[i]:
        count += 1
        array[i] -= 1
    temp = array[i]

print(count)