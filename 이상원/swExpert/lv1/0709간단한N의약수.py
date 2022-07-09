'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2
'''


n = int(input())
half = n // 2
result = []
for num in range(1, half):
    if n % num == 0:
        result.append(num)
        result.append(n//num)
result = list(set(result))
result.sort()
print(' '.join(map(str, result)))
