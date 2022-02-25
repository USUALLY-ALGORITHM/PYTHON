# 소인수분해 (https://www.acmicpc.net/problem/11653)

N = int(input())

i = 2
while N != 1:
    if N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1