'''
https://www.acmicpc.net/problem/7568
'''
import sys


inputs = sys.stdin.readline

n = int(inputs())
arr = []
for i in range(n):
    w, h = map(int, inputs().split())
    arr.append([w, h])

answer = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    answer.append(cnt+1)

for item in answer:
    print(item)
