# 신입 사원 (https://www.acmicpc.net/problem/1946)
# 혼자 풀었나? × (문제를 꼼꼼히 읽자..)

import sys

T = int(sys.stdin.readline())
people = []

for _ in range(T):
    N = int(input())

    people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    people.sort()

    cnt = 1
    max = people[0][1]

    for i in range(1, N):
        if max > people[i][1]:
            cnt += 1
            max = people[i][1]

    print(cnt)

# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801946%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90
# for i in range(N):
    #     g1, g2 = map(int, sys.stdin.readline().split())
    #     people.append([g1, g2])