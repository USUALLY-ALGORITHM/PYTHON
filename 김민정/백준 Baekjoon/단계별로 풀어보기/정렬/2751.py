# 수 정렬하기 2 (https://www.acmicpc.net/problem/2751)

import sys

N = int(input())
array = []

for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
for i in range(N):
    print(array[i])