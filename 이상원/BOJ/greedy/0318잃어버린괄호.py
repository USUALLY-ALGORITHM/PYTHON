'''
https://www.acmicpc.net/problem/1541

세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

55-50+40

'''
# import sys


# inputs = sys.stdin.readline

# getInput = str(inputs().split('-'))

# if '-' in getInput:
#     exceptSub = getInput.split('-')
#     _plus = exceptSub[-1][:-1]
#     plus = sum(map(int, _plus.split('+')))
#     subNum = int(exceptSub[0])
#     for item in exceptSub[1:-1]:
#         subNum -= int(item)
#     print(subNum - plus)


# else:
#     splitInput = map(int, getInput.split('+'))
#     print(sum(splitInput))
# ! 런타임 에러

# # > +가 있는 경우 함수
# def isPlus(plusString: str):
#     splitPlus = map(int, plusString.split('+'))
#     return sum(splitPlus)


# # > - 를 기준으로 split
# if '-' in getInput:
#     splitByMinus = getInput.split('-')
#     answer = int(splitByMinus[0])
#     for item in splitByMinus[1:]:
#         if '+' in item:
#             answer -= isPlus(item)
#         else:
#             answer -= int(item)
#     print(answer)
# else:
#     print(isPlus(getInput))
# ! 런타임 에러 ...
'''
최솟값을 만들기 위해서는 - 기준으로 괄호를 치면 된다.
예를 들어
55 - 50 + 40 - 30 + 20
위와 같이 입력 했을때, - 기준으로 55 - (50 + 40) - (30 + 20) 이렇게 괄호를 쳤을때 최솟값이 된다.
그래서 입력을 받을때 - 기준으로 입력을 받아준다.
위와 같이 입력을 받았을때 [‘55’, ‘50 + 40’, ‘30 + 20’] 이렇게 입력을 받게 되는데 각 원소에 있는 숫자들을 계산해주고 맨 처음의 원소는 더해주고 나머지는 빼준다.
'''
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
