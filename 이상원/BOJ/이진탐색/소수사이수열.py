"""
5
10
11
27
2
492170

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


def numPrime(n):
    left = n - 1
    right = n + 1

    while True:
        if isPrime(left):
            break
        left -= 1

    while True:
        if isPrime(right):
            break
        right += 1
    return right - left


inputs = sys.stdin.readline

n = int(inputs())
arr = [0] * n
for i in range(n):
    nums = int(inputs())
    if isPrime(nums):
        print(0)
    else:
        print(numPrime(nums))
