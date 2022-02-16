"""
https://www.acmicpc.net/problem/3009
"""

import collections


xDot = []
yDot = []

for i in range(3):
    x, y = map(int, input().split())
    xDot.append(x)
    yDot.append(y)

xCnt = collections.Counter(xDot)
yCnt = collections.Counter(yDot)

answer = [0, 0]
for _x, _y in zip(xCnt.items(), yCnt.items()):
    if _x[1] == 1:
        answer[0] = _x[0]
    if _y[1] == 1:
        answer[1] = _y[0]

for i in answer:
    print(i, end=" ")
