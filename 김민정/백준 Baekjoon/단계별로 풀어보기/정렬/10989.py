# 수 정렬하기 3 (https://www.acmicpc.net/problem/10989)

import sys

N = int(input())
array = [0] * 10001

for _ in range(N):
    array[int(sys.stdin.readline())] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)