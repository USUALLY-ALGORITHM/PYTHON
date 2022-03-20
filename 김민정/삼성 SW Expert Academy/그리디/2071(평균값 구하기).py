# 평균값 구하기 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&)

T = int(input())

for i in range(T):
    sum = 0
    array = list(map(int, input().split()))
    for data in array:
        sum += data
    print(f'#{i + 1}', round(sum / 10))