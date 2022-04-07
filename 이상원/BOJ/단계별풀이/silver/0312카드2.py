'''
https://www.acmicpc.net/problem/2164
'''
''' 
* idx 기준 짝수는 버리고 
* 홀수는 밑으로 
'''


import collections
import sys
inputs = sys.stdin.readline

n = int(inputs())

deque = collections.deque()

for i in range(n):
    deque.append(i+1)

while len(deque)>1:
    deque.popleft()
    nums = deque.popleft()
    deque.append(nums)    
    
print(deque[0])