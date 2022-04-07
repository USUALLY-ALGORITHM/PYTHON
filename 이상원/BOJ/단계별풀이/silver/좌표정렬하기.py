"""
https://www.acmicpc.net/problem/11650
"""

import sys

sysIn = sys.stdin.readline

n = int(sysIn())
arr = []
for i in range(n):
    x, y = map(int, sysIn().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[0], x[1]))
for i, j in arr:
    print(f"{i} {j}")
