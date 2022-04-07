def solution(n, lst):
    lst.sort()

    result = 0
    idx_time = 0
    for i in lst:
        idx_time += i
        result += idx_time
    print(result)


if __name__ == '__main__':
    n = 5
    lst = [3, 1, 4, 3, 2]
    print(solution(n, lst))
