def solution(n):
    '''
    :param n: 거스름돈
    :return: 동전 개수
    '''
    count = 0

    # 큰 단위 화폐부터 차례대로 확인
    array = [500, 100, 50, 10]

    for coin in array:
        count += n // coin
        n %= coin

    return count


if __name__ == '__main__':
    n = 1260
    print(solution(n))
