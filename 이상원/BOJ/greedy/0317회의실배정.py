'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 
각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

'''
# import sys


# inputs = sys.stdin.readline
# n = int(inputs())

# timeline = [[] for _ in range(n)]

# for i in range(n):
#     start, end = map(int, inputs().split())
#     timeline[i].append([start, end])

# compare = timeline[:]
# for i in range(n):
#     for idx in range(n):
#         if timeline[i][-1][1] <= compare[idx][0][0]:
#             timeline[i].append(compare[idx][0])

# maxCount = 0
# for i in timeline:
#     if maxCount <= len(i):
#         maxCount = len(i)

# print(maxCount)
# ! 시간 초과 ...
# timeline = []
# for i in range(n):
#     start, end = map(int, inputs().split())
#     timeline.append([start, end])

# timeline.sort(key=lambda x: x[0])
# timeline.sort(key=lambda x: x[1])

# answer = 1

# endTime = 0
# for st, en in timeline:
#     if endTime <= st:
#         answer += 1
#         endTime = st
# print(answer)


n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
