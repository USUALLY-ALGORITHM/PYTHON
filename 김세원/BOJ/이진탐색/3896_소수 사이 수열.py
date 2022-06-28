import sys

input = sys.stdin.readline
n = int(input())

#최대값
max_num = 1300001

#소수 참, 거짓 기록 배열
num = [0]*max_num

#정답 기록 배열
answer = []
#소수 기록 배열
prime = []

#에라토스테네스의 체
for i in range(2, max_num):
    if num[i] != 0:
        continue

    for j in range(i*2, max_num, i):
        num[j] = 1

#소수 배열에 append
for i in range(2, max_num):
    if not num[i]:
        prime.append(i)

length = len(prime)

#이분 탐색
def search(key):
    l = 2
    r = length - 1

    while l <= r:
        mid = (l + r)//2

        if prime[mid] >= key:
            r = mid - 1
        else:
            l = mid + 1

    return l

for i in range(n):
    m = int(input())

    if not num[m]:
        answer.append(0)
        continue

    value = search(m)

    answer.append(prime[value] - prime[value - 1])

for i in range(n):
    print(answer[i])
