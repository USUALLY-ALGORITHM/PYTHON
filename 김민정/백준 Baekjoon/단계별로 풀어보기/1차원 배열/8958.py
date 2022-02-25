# OX퀴즈 (https://www.acmicpc.net/problem/8958)

N = int(input())

for i in range(N):
    score, count = 0, 1 # score : 최종 점수, count : 정답 시 배점 초기값
    result = input()
    for i in range(len(result)):
        if result[i] == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)