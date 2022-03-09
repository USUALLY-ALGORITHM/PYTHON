'''
https://www.acmicpc.net/problem/1057
'''
import sys


inputs = sys.stdin.readline

n, kim, lim = map(int, inputs().split())

cnt = 0
while kim != lim:
    kim -= kim//2
    lim -= lim//2
    cnt += 1

print(cnt)
