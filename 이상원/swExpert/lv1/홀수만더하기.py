'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&

3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1

'''
# import sys


# inputs = sys.stdin.readline

# test = int(input())

# arrSet = []
# for item in range(test):
#     arr = list(map(int, input().split()))
#     arrSet.append(arr)

# for item in arrSet:
#     num = 0
#     for j in item:
#         if j % 2 == 1:
#             num += j
#     print(num)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
answer = []

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    num = 0
    for j in arr:
        if j % 2 == 1:
            num += j
    answer.append(num)
print('\n')
for i in range(T):
    print(f'#{i+1} {answer[i]}')
