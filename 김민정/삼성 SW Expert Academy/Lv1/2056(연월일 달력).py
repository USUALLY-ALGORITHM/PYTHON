# 연월일 달력 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1)

T = int(input())

for i in range(T):
    num = input()
    year = int(num[0:4])
    month = int(num[4:6])
    day = int(num[6:8])
    print('#%s' % (i + 1), end=' ')

    if month < 1 or month > 12:
        print(-1)
        continue

    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                print(-1)
                continue

        elif month == 2:
            if day < 1 or day > 28:
                print(-1)
                continue
        else:
            if day < 1 or day > 30:
                print(-1)
                continue
    print('%04d/%02d/%02d' %(year, month, day))