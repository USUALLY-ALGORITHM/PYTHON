"""
정수 x의 각 자리가 등차 수열이면 그 수를 한 수 라고 한다 

"""


def checkNum(n):
    numStr = str(n)
    lst = []
    for i in range(len(numStr) - 1):
        lst.append(int(numStr[i]) - int(numStr[i + 1]))
    resLst = list(set(lst))
    if len(resLst) == 1:
        return True
    else:
        return False


n = int(input())
result = 0

for i in range(1, n + 1):
    if i < 99:
        result += 1
    elif checkNum(i):
        result += 1

print(result)
