"""
https://www.acmicpc.net/problem/2775
"""


n = int(input())
for _ in range(n):
    k = int(input()) + 1
    n = int(input())
    arr = [0] * n

    for floor in range(k):
        for addr in range(n):
            if arr[addr] == 0:
                arr[addr] += addr + 1
            else:
                if addr == 0:
                    continue
                else:
                    arr[addr] += arr[addr - 1]
    print(arr[-1])
