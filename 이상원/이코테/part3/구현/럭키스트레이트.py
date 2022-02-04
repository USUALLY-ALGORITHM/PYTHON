"""
백준 18406
현재 캐릭터 점수 = N
자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 
오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황 

123402

7755
"""

n = str(input())


def mysolution(n):

    half = len(n) // 2

    left = n[:half]
    right = n[half:]

    left_result = 0
    right_result = 0

    for l, r in zip(left, right):
        left_result += int(l)
        right_result += int(r)

    print("LUCKY" if left_result == right_result else "READY")


mysolution(n)
