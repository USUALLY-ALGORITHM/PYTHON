# 홀수만 더하기 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1)

T = int(input())

for i in range(T):
    sum = 0
    array = list(map(int, input().split()))
    for data in array:
        if data % 2 != 0:
            sum += data
    print(f'#{i + 1}', sum)