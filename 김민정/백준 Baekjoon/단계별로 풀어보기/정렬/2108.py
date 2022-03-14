# 통계학 (https://www.acmicpc.net/problem/2108)

import sys
from collections import Counter

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

# 산술 평균
print(round(sum(array) / N))

# 중앙값
array.sort()
print(array[N // 2])

# 최빈값
count = Counter(array).most_common()
if len(count) > 1 and count[0][1] == count[1][1]: # 최빈값 2개 이상
    print(count[1][0])
else:
    print(count[0][0])

# 범위
print(max(array) - min(array))
