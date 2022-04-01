# 로프 (https://www.acmicpc.net/problem/2217)

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array.sort(reverse=True)

result = []
for i in range(N):
    result.append(array[i] * (i + 1))
print(max(result))

# https://jitolit.tistory.com/134
# 문제 이해가 안돼서 찾아봤어요 ㅠ-ㅠ. .