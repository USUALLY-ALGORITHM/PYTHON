"""
그룹 단어 존재하는 모든 문자에 대해 
각 문자가 연속해서 나타나는 경우를 말함 
ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
 
"""

cnt = 0


def checkWord(word):
    pass


n = int(input())

for i in range(n):
    word = str(input())
