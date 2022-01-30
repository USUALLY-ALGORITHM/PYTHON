"""
모험가 N명이 있다 
공포도 측정 - 위험 상황에서 제대로 대처 능력 떨어짐
동빈이는 그룹을 안전하게 구성하고자 함 
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야 
여행을 떠날 수 있음
최대 만들수 있는 그룹은??

5
2 3 1 2 2
"""

import collections


N = int(input())
fear = list(map(int, input().split()))
result = 0

cnt = collections.Counter(fear)

for item in cnt:
    if item <= cnt[item]:
        result += 1

print(result)
