import itertools
import sys


inputs = sys.stdin.readline

arr = [0 for i in range(9)]

for item in range(9):
    arr[item] = int(inputs())

listSum = sum(arr)

combinationList = list(itertools.combinations(arr, 2))


for item in combinationList:
    if listSum - sum(item) == 100:
        delNum = item
        break
for item in arr:
    if item in delNum:
        continue
    print(item)
