# 1대1 가위바위보 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2)

a, b = map(int, input().split())

if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("A")
else:
    print("B")