'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2

'''
gameTable = {1: 3, 2: 1, 3: 2}
a, b = map(int, input().split())

print('A' if gameTable[a] == b else "B")
