'''
https://www.acmicpc.net/problem/4948
'''


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
inputArr = []
while True:
    n = int(input())
    if n == 0:
        break
    inputArr.append(n)

print(inputArr)

arr = []
answer = []
for item in inputArr:
    end = item*2
    for j in range(item, end+1):
        if isPrime(j):
            arr.append(j)
    answer.append(len(arr))

for i in answer:
    print(i)
