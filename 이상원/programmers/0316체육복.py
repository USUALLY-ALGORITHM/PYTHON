'''
https://programmers.co.kr/learn/courses/30/lessons/42862
'''


def solution(n, lost, reserve):
    answer = 0
    studentList = [1] * (n+1)

    for item in lost:
        studentList[item] -= 1
    for item in reserve:
        studentList[item] += 1

    # for i in range(n+1):
    #     if i in reserve:
    #         studentList[i] += 1
    #     elif i in lost:
    #         studentList[i] -= 1

    for i in range(1, n+1):
        if studentList[i] == 2:
            if i > 0 and studentList[i-1] == 0:
                studentList[i] -= 1
                studentList[i-1] += 1
            elif i < n and studentList[i+1] == 0:
                studentList[i] -= 1
                studentList[i+1] += 1

    studentList = studentList[1:]
    for i in studentList:
        if i != 0:
            answer += 1
    return answer


if __name__ == '__main__':
    n = [5, 5, 3, 6]
    lost = [
        [2, 4],
        [2, 4],
        [3],
        [1, 3, 6]
    ]
    reserve = [
        [1, 3, 5],
        [3],
        [1],
        [3, 4, 5]
    ]

    for _n, _lost, _reserve in zip(n, lost, reserve):
        print(solution(_n, _lost, _reserve))
