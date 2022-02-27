# 문자열 반복 (https://www.acmicpc.net/problem/2675)

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)

    for j in range(len(S)):
        print(R * S[j], end='')
    print()