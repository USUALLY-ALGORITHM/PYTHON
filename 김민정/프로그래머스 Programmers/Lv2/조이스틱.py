def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i in range(len(name)):
        answer += min(ord(name[i])-ord("A"), ord("Z")+1-ord(name[i]))

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min([min_move, 2 * i + len(name) -
                       next, i + 2 * (len(name) - next)])
    answer += min_move

    return answer


# https://zoozoozoo.tistory.com/110
'''
1) 가장 기본으로 그냥 무작정으로 문자열 끝까지 이동하는 경우를 초기 값으로 설정해둔다.

2) 처음부터 해당 문자까지 왕복으로 왔다갔다 + 연속된 A의 문자 인덱스가 끝난 지점에서 전체길이 뺀값

3) 시작부터 연속된 A의 문자 인덱스가 끝난 지점에서 전체길이 뺀값 왕복 + A나오기 까지 인덱스
'''
