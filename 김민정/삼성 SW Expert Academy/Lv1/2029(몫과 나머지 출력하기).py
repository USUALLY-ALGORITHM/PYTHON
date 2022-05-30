# 몫과 나머지 출력하기 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2&&&&&&&&&&)

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(f'#{i + 1}', a // b, a % b)
