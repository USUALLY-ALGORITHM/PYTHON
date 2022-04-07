"""https://www.acmicpc.net/problem/1181
"""


import sys


n = int(input())

arr = [""] * n
for i in range(n):
    arr[i] = sys.stdin.readline().rstrip()

setList = list(set(arr))
sortedList = sorted(setList, key=lambda x: (len(x), x))

for i in sortedList:
    print(i)
