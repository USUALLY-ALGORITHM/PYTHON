'''
https://www.acmicpc.net/problem/2798

숫자 m을 외친다 
제한 시간에 n장의 카드 중 3개를 골라야 한다  고른 카드의 합은 m이 넘지 않으면서 m과 최대한 가깝게 
m을 넘지 않으면서 m에 가까운 카드 3장의 합을 출력
'''
import itertools
import sys


inputs = sys.stdin.readline
n, m = map(int, inputs().split())

arr = list(map(int, inputs().split()))

comnbArr = list(itertools.combinations(arr, 3))

maxSum = 0
for _sum in comnbArr:
    arrSum = sum(_sum)
    if arrSum > m:
        continue

    elif arrSum > maxSum:
        maxSum = arrSum

print(maxSum)
