# 좌표 압축 (https://www.acmicpc.net/problem/18870)

import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array_rank = sorted(list(set(array)))

num_dict = {}
for i in range(len(array_rank)):
    num_dict[array_rank[i]] = i

for i in array:
    print(num_dict[i], end=' ')

# https://steadily-worked.tistory.com/591