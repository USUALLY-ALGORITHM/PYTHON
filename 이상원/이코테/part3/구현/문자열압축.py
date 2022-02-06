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


def booksolution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j : j + step]:
                count += 1
            # 다른 문자열이 나오면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]  # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer


s = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

for i in s:
    print(booksolution(i))
