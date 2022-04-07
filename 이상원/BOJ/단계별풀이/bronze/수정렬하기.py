"""
https://www.acmicpc.net/problem/2750
n개의 수가 주어졋을대 오름차순 정렬
"""

n = int(input())

arr = [0]
for i in range(n):
    num = int(input())
    if arr[-1] < num:
        arr.append(num)
    else:
        arr.insert()

# -------------------------------

import sys

n = int(input())  # 입력받는 수의 개수 n
unsorted_list = []
sorted_list = []

for i in range(n):
    # > sys 입력
    a = int(sys.stdin.readline())
    unsorted_list.append(a)

sorted_list = sorted(set(unsorted_list))
for i in sorted_list:
    # > sys out
    sys.stdout.write(str(i) + "\n")
