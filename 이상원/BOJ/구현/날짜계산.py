"""
수 3개를 이용해 연도를 나타냄
지구 태양 달을 나타냄
지구 E 태양 S 달 M (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
1년 = 1 1 1
1년이 지나면 세 수는 1씩 증가한다
범위를 넘어가면 1이 된다 

1 16 16

1 2 3

"""


from itertools import starmap
import sys

from dbus import StarterBus


def timeout():
    nums = list(map(int, input().split()))
    e_start, s_start, m_start = 1, 1, 1
    add_list = [15, 28, 19]
    cnt = 0

    idx = nums.index(min(nums))
    add_num = 15
    s = nums[0]

    while True:
        cnt += 1
        e_start += add_num + s - 1
        # s_start += add_num + s - 1
        # m_start += add_num + s - 1

        remain_e = e_start % 15
        remain_s = e_start % 28
        remain_m = e_start % 19

        if remain_e == nums[0] and remain_m == nums[2] and remain_s == nums[1]:
            cnt *= add_num
            break
    print(cnt + 1)


def solution():
    e, s, m = [int(x) for x in sys.stdin.readline().split()]
    start_e, start_s, start_m = 1, 1, 1

    cnt = 0

    while True:
        cnt += 1
        if start_e == e and start_s == s and start_m == m:
            break
        start_e += 1
        start_s += 1
        start_m += 1

        if start_e == 16:
            start_e = 1
        if start_s == 29:
            start_s = 1
        if start_m == 20:
            start_m = 1

    print(cnt)


# timeout()
solution()
