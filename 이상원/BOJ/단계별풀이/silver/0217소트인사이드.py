"""https://www.acmicpc.net/problem/1427
"""
n = str(input())
sortedN = sorted(n, reverse=True)
for i in sortedN:
    print(i, end="")
