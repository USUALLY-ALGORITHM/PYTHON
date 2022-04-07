'''
https://www.acmicpc.net/problem/2577
'''
import collections
import sys


mul = 1

inputs = sys.stdin.readline

for i in range(3):
    mul *= int(inputs())

numDict = collections.defaultdict(int)

for i in str(mul):
    numDict[i] += 1

for i in range(10):
    if numDict[str(i)]:
        print(numDict[str(i)])
    else:
        print(0)
