'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2

3
9 2
15 6
369 15

'''

T = int(input())

for item in range(T):
    a, b = map(int, input().split())
    divide = a // b
    remain = a % b
    print(f'#{item + 1} {divide} {remain}')
