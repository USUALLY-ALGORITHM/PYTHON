# 골드바흐의 추측 (https://www.acmicpc.net/problem/9020)

import sys
input = sys.stdin.readline

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for i in range(n//2, -1, -1):
        if isPrime(i) and isPrime(n-i):
            print(i, n-i)
            break