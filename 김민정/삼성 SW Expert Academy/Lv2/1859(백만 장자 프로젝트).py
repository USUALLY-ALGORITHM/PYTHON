# 백만 장자 프로젝트 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&)
# 혼자 풀었나? × (🤢)

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    max = price[-1]
    cnt = 0

    for j in range(len(price)-1, -1, -1):
        if max > price[j]:
            cnt += max - price[j]
        else:
            max = price[j]
    print('#{} {}'.format(i, cnt))