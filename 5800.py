# 성적 통계 (https://www.acmicpc.net/problem/5800)

K = int(input())

for i in range(1, K + 1):
    print('Class %d' %(i))
    score = list(map(int, input().split()))
    N = score[0]
    score = score[1:]
    score.sort(reverse = True)

    max_gap = 0
    for j in range(N - 1):
        gap = abs(score[j] - score[j + 1])
        if gap > max_gap:
            max_gap = gap
    print('Max %d, Min %d, Largest gap %d' %(score[0], score[-1], max_gap))