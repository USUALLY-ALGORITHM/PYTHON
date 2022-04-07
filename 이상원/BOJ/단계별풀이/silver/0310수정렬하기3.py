'''
https://www.acmicpc.net/problem/10989
# '''

# > 메모리 초과
import heapq
import sys


inputs = sys.stdin.readline

n = int(inputs())
q = []
arr = []
for i in range(n):
    nums = int(inputs())
    heapq.heappush(q, nums)

for i in q:
    print(i)


n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
