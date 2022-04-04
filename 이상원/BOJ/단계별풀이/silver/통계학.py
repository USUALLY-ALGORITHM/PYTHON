"""
https://www.acmicpc.net/problem/2108

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이

"""
import collections
import math
import sys


inputs = sys.stdin.readline

n = int(inputs())
arr = [0] * n
for i in range(n):
    arr[i] = int(inputs())

arithMean = round(sum(arr) / n)

arr.sort()
mid = arr[(n - 1) // 2]

_maxCnt = collections.Counter(arr)
maxCnt = sorted(_maxCnt.items(), key=lambda x: (x[1], -x[0]), reverse=True)


arange = arr[-1] - arr[0]
print(arithMean)
print(mid)
if len(arr) > 1 and maxCnt[0][1] == maxCnt[1][1]:
    print(maxCnt[1][0])
else:
    print(maxCnt[0][0])
print(arange)
