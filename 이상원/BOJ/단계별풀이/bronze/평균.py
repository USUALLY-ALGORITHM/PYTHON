'''
https://www.acmicpc.net/problem/1546
'''
import sys


inp = sys.stdin.readline

n = int(inp())
scores = list(map(int, inp().split()))

maxScore = max(scores)
sumScore = 0
for i in scores:
    sumScore += i / maxScore * 100

print(sumScore/n)
