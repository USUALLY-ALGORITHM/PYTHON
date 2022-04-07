'''
https://www.acmicpc.net/problem/18870
'''
import collections
import sys


inputs = sys.stdin.readline
n = int(inputs())

arr = list(map(int, inputs().split()))

setArr = set(arr[:])
setArrSort = sorted(setArr)
arrDict = collections.defaultdict()

rank = 0
for i in setArrSort:
    arrDict[i] = rank
    rank += 1

for i in arr:
    print(arrDict[i], end=' ')
