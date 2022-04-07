'''
https://www.acmicpc.net/problem/2217

2
10
15

'''
import sys


inputs = sys.stdin.readline
n = int(inputs())
nums = []
for item in range(n):
    nums.append(int(inputs()))
nums.sort(reverse=True)
answer = []
for i in range(n):
    answer.append(nums[i]*(i+1))
print(max(answer))
