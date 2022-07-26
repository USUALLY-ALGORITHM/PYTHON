# A -> B (https://www.acmicpc.net/problem/16953)
# 혼자 풀었나? × (이걸 어케 생각해요)

A, B = map(int, input().split())
cnt = 1

while True:
    if B == A:
        break
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        cnt = -1
        break
    else:
        if B % 10 == 1:
            B //= 10
            cnt += 1
        else:
            B //= 2
            cnt += 1
print(cnt)

# https://alpyrithm.tistory.com/118