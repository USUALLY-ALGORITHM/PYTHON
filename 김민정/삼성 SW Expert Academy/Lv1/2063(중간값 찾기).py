# 중간값 찾기 (https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&)

N = int(input())
array = list(map(int, input().split()))
array.sort()

for i in range(N):
    if i == N//2:
        print(array[i])
        break