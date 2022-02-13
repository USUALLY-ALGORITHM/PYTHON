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


def bookSolution(n):
    length = len(n)
    summary = 0

    # 왼쪽 부분 자릿수 합 더하기
    for i in range(length // 2):
        summary += int(i)

    # 왼쪽 부분 자릿수 합 빼기
    for i in range(length // 2):
        summary -= int(i)

    # 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
    if summary == 0:
        print("LUCKY")
    else:
        print("READY")


mysolution(n)
bookSolution(n)
