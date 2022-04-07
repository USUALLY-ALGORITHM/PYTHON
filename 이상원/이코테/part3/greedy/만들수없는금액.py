'''
동빈이는 N개의 동전을 가지고 있다 
N개의 동전을 이용해서 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램 

N = 5 3 5 7원 있다고 하면 
만들수 없는 가장 작은 금액은 1원이다 

5
3 2 1 1 9
'''


import collections
import itertools


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 1

for item in arr:
    if answer < item:
        break
    answer += item

print(answer)
