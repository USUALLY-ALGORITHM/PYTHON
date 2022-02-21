"""
https://www.acmicpc.net/problem/1431
"""

n = int(input())

arr = []
for i in range(n):
    arr.append(str(input()))


def numSum(word):
    cnt = 0
    for i in word:
        if i.isdigit():
            cnt += int(i)
    return cnt


arr.sort(key=lambda x: (len(x), numSum(x), x))
for i in arr:
    print(i)
