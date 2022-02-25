# 별 찍기 -2 (https://www.acmicpc.net/problem/2439)

N = int(input())

for i in range(N):
    print(' ' * (N - (i + 1)) + '*' * (i + 1))