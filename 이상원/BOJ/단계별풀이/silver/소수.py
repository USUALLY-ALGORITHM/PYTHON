"""
https://www.acmicpc.net/problem/2581
"""

import sys


def isPrime(a):
    # *소수 판별
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


inputs = sys.stdin.readline

m = int(inputs())
n = int(inputs())
arr = []
for i in range(m, n + 1):
    if isPrime(i):
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
