# 수 정렬하기 ()

N = int(input())
array = []

for i in range(N):
    array.append(int(input()))

array.sort()
for i in range(N):
    print(array[i])