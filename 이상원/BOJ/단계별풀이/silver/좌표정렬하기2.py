'''
https://www.acmicpc.net/problem/11651
'''

import sys

sysIn = sys.stdin.readline

n = int(sysIn())
arr = []
for i in range(n):
    x, y = map(int, sysIn().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))
for i, j in arr:
    print(f"{i} {j}")
