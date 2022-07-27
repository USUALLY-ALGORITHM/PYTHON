# 간단한 369게임(https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
# 혼자 풀었나? △ (count 함수를 생각 못했다!)

N = int(input())

for i in range(1, N + 1):
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print('-' * clap, end=' ')