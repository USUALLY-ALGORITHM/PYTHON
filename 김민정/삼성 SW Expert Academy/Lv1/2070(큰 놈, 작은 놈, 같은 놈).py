# 큰 놈, 작은 놈, 같은 놈 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&)

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    if x > y:
        print(f'#{i + 1}', '>')
    elif x == y:
        print(f'#{i + 1}', '=')
    elif x < y:
        print(f'#{i + 1}', '<')