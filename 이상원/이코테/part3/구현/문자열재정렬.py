"""
알파벳 대문자와 숫자로 구성된 문자열이 입력
알파벳을 오름차순 정렬, 모든 숫자를 더한 값을 출력

K1KA5CB7

"""

n = str(input())


def mysolution(n):
    sortedN = sorted(n)


    result = [[] for _ in range(2)]

    for word in n:
        if word.isalpha():
            result[0].append(word)
        else:
            result[1].append(int(word))

    res = sorted(result[0])
    sum_num = sum(result[1])

    print(f'{"".join(res)}{sum_num}')

mysolution(n)