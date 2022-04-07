"""
N개의 원소를 포함하는 수열이 오름차순으로 정렬되어 있다 
x가 등장하는 횟수를 계산하라 
logN으로 알고리즘으로 설계 해야 함 

7 2
1 1 2 2 2 2 3

"""
import collections
from posixpath import split
import sys


inputs = sys.stdin.readline
n, x = map(int, inputs().split())
arr = list(map(int, inputs().split()))

cnt = collections.Counter(arr)
print(cnt[x])


from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())  # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split()))  # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)


"""특정 범위에 속하는 원소의 개수 구하기"""
from bisect import bisect_left, bisect_right


def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i


nums = [
    -1,
    -3,
    5,
    5,
    4,
    7,
    1,
    7,
    2,
    5,
    6,
]  # 5 ~ 7 을 갖는 요소의 개수 구하기
nums.sort()  # 정렬은 필수
print(calCountsByRange(nums, 5, 7))
""" 결과값 6 """
