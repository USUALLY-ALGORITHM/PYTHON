"""
인덱스 번호와 값이 동일한 고정점을 찾아라 
logN의 시간 복잡도로 해결 

5
-15 -6 1 3 7
"""

import sys


def bst(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if mid == arr[mid]:
        return mid

    if arr[mid] < mid:
        return bst(arr, mid + 1, end)
    else:
        return bst(arr, start, mid - 1)


inputs = sys.stdin.readline
n = int(inputs())

arr = list(map(int, inputs().split()))
idx = bst(arr, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if idx == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else:
    print(idx)
