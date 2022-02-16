"""
https://www.acmicpc.net/problem/2775
"""


def getNumOfPeople(apt, i, j):
    if i == 0:
        apt[i][j] = j + 1
    elif j == 0:
        apt[i][j] = 1
    else:
        apt[i][j] = apt[i][j - 1] + apt[i - 1][j]


apt = [[0] * 14 for _ in range(14)]


n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())

    for i in range(14):
        for j in range(14):
            getNumOfPeople(apt, i, j)
        if i == k and j == n - 1:
            break
    print(apt[k][n - 1])
