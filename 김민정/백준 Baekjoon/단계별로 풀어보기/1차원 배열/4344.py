# 평균은 넘겠지 (https://www.acmicpc.net/problem/4344)

C = int(input())

for i in range(C):
    test = list(map(int, input().split()))
    avg = (sum(test) - test[0]) / test[0]
    count = 0
    for j in test[1:]:
        if j > avg:
            count += 1
    print("%.3f%%" %(count / test[0] * 100)) #  print("{:.3f}%".format((count / test[0] * 100)))