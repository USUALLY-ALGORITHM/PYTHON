"""
N명의 사람이 매일 아침 한 줄로 선다 
자기보다 큰 사람이 왼쪽에 몇 명 있었는지만 기억한다 
키가 1인 사람부터 차례대로 자기보다 큰 사람이 왼쪽에 몇명 있었는지 주어진다 


4
2 1 1 0
"""

from __future__ import print_function
from audioop import reverse
from linecache import getline


n = int(input())
line = list(map(int, input().split()))

line_list = [0] * n


def checkIdx(lineList, id, leftNum):
    """idx check

    Args:
        lineList (list): 정답 리스트
        id (int): 사람 키
        leftNum (int): 왼쪽에 몇명 있는지
    """
    if lineList[leftNum] != 0:
        return checkIdx(lineList, id, leftNum + 1)
    else:
        lineList[leftNum] = id
        return lineList


def error(lstLine, getLine):
    for i, item in enumerate(getLine):
        person_id = i + 1
    lstLine = checkIdx(getLine, person_id, item)

    print(" ".join(map(str, lstLine)))

    # ---------------------------------------------------------


line_dict = {}
for i, item in enumerate(line):
    line_dict[i + 1] = item

sorted_list = sorted(line_dict.items(), key=lambda val: val[0], reverse=True)


result = [0]
for person, leftNum in sorted_list:
    result.insert(leftNum, person)

result.remove(0)
print(" ".join(map(str, result)))


# 답은 나오는데 틀렸다고 나옴
# error(line_list, line)
