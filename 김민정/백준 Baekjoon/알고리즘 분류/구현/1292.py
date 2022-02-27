# 쉽게 푸는 문제 (https://www.acmicpc.net/problem/1292)

A, B = map(int, input().split())

array = [0]
for i in range(B + 1):
    for j in range(i):
        array.append(i)

print(sum(array[A:B + 1]))