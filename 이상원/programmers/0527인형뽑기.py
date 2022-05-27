'''
https://programmers.co.kr/learn/courses/30/lessons/64061

'''


def solution(board, moves):
    answer = 0
    bucket = []
    for item in moves:
        idx = item - 1
        for row in range(len(board)):
            if board[row][idx] == 0:
                continue
            else:
                bucket.append(board[row][idx])
                board[row][idx] = 0
            if len(bucket) > 1 and (bucket[-1] == bucket[-2]):
                print(bucket)
                bucket.pop()
                bucket.pop()
                answer += 2
    return answer


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
        0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    for item in board:
        print(item)
    print('--')

    print(solution(board, moves))
