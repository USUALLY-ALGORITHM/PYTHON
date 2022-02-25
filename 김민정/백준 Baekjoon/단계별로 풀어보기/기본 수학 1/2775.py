# 부녀회장이 될거야 (https://www.acmicpc.net/problem/2775)

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n + 1)] # 한 호수에 사는 사람 수

    for _ in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]
    print(people[-1])

"""
0층 : 1 2 3 4 5 6 ...
1층 : 1 3 6 10 15 21 ...
2층 : 1 4 10 20 35 56 ...

d[i][j] = d[i - 1][j] + d[i][j - 1]
"""