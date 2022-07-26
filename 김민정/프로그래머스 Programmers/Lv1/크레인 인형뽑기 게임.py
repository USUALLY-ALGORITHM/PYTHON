def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])    # 0이 아닌 경우만 뽑아 stacklist(바구니) 에 넣음
                board[j][i-1] = 0    # 뽑힌 숫자(인형)은 0으로 변경

                # stacklist(바구니)에 인형이 2개 이상 있을때마다 확인
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:    # 맨 마지막 두 개의 숫자가 같으면
                        stacklist.pop(-1)    #
                        stacklist.pop(-1)    # 그 두개를 pop
                        answer += 2
                break

    return answer