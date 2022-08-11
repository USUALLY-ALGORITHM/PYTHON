'''
https://www.acmicpc.net/problem/1946


2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1


'''


import sys


def getNumOfPerson(arr, n):
    first = sorted(arr, key=lambda x: x[0])
    second = sorted(arr, key=lambda x: x[1])
    cnt = 0

    for f, s in zip(first, second):
        if f == s:
            continue
        else:
            cnt += 1

    print(cnt)


inputs = sys.stdin.readline

t = int(inputs())
for test in range(t):
    n = int(inputs())
    arr = []
    for item in range(n):
        paper, interview = map(int, inputs().split())
        arr.append([paper, interview])
    getNumOfPerson(arr, n)
