"""
https://www.acmicpc.net/problem/1978

4
1 3 5 7

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

n = int(inputs())
arr = list(map(int, inputs().split()))
cnt = 0
for i in arr:
    if isPrime(i):
        cnt += 1
print(cnt)
