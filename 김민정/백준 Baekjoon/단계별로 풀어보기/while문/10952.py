# A + B - 5 (https://www.acmicpc.net/problem/10952)

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A + B)