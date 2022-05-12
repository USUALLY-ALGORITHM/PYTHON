'''
https://www.acmicpc.net/problem/1697

5 17

'''

n, k = map(int, input().split())

line = [x for x in range(100000)]

sec = 0

for item in range(len(line)):
    if n == k:
        print(sec)
        break
    