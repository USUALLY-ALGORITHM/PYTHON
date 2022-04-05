'''
https://www.acmicpc.net/problem/13305

4
2 3 1
5 2 4 1

'''

import sys


inputs = sys.stdin.readline

n = int(inputs())
roadLengh = list(map(int, inputs().split()))
price = list(map(int, inputs().split()))

answer = 0
cost = price[0]

for item in range(n-1):
    # 0 1 2 -> item
    if cost > price[item]:
        cost = price[item]
    answer += cost*roadLengh[item]

print(answer)
