"""
n명의 학생 
학생 이름 성적 
성적이 낮은 순서대로 학생 이름 출력 

2
홍길동 95
이순신 77
"""

n = int(input())


def mysol(n):
    dict = {}
    for i in range(n):
        name, score = map(str, input().split())
        dict[name] = int(score)

    dictSort = sorted(dict.items(), key=lambda x: x[1])
    for i in dictSort:
        print(i[0], end=" ")


def bookSol(n):
    array = []

    for i in range(n):
        input_data = input().split()
        array.append((input_data[0], int(input_data[1])))

    array = sorted(array, key=lambda std: std[1])

    for i in array:
        print(i, end=" ")
