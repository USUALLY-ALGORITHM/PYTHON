# 나이순 정렬(https://www.acmicpc.net/problem/10814)

N = int(input())

member = []
for i in range(N):
    age, name = input().split(' ')
    member.append([int(age), name])

member = sorted(member, key=lambda x:x[0])

for i in member:
    print(i[0], i[1])