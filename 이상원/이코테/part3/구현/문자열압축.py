"""
https://programmers.co.kr/learn/courses/30/lessons/60057
카카오 문제 
문자열 압축
같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현
aabbaccc는 2a2ba3c로 나타냄 
1은 생략함 
ababcdcdababcdcd 은 

abc abc abc abc de de de de de de
4abcdedededede

"""


def solution(s):
    answer = 0
    pattern = []
    compare_with_pattern = []

    for i in s:
        pattern.append(i)
        if pattern[0] == i:
            pattern.pop()
            compare_with_pattern.append(pattern)
            pattern = []
            pattern.append(i)
        else:
            pattern.append(i)
    print(compare_with_pattern)

    return answer


s = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

for i in s:
    print(solution(i))
