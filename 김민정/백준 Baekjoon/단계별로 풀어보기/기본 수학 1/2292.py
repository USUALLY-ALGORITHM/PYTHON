# 벌집 (https://www.acmicpc.net/problem/2292)

N = int(input())

count = 1
while N > 1:
    N -= 6 * count
    count += 1
print(count)