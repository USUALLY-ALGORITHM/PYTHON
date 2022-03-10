'''
https://www.acmicpc.net/problem/11047
'''
import sys

inputs = sys.stdin.readline
n, k = map(int, inputs().split())
arr = [0]*n
for i in range(n):
    wons = int(inputs())
    arr[i] = wons

arr.sort(reverse=True)

cnt = 0
for i in arr:
    cntWon = k//i
    cnt += cntWon
    k -= cntWon*i
    if k == 0:
        break


print(cnt)
