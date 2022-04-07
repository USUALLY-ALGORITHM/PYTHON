'''
https://www.acmicpc.net/problem/11866
'''

import collections
import sys


inputs = sys.stdin.readline
n, k = map(int, inputs().split())

deque = collections.deque()
for i in range(n):
    deque.append(i+1)

answer = []
while deque:
    for i in range(k-1):
        deque.append(deque.popleft())
    answer.append(deque.popleft())

print("<", end='')
for i in range(len(answer)-1):
    print("%d, " % answer[i], end='')
print(answer[-1], end='')
print(">")
