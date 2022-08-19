array = [int(input()) for _ in range(9)]

# 9명의 숫자를 다 더한 후, 100을 빼서 범인 두 명을 구한다.
for i in range(9):
    for j in range(i + 1, 9):
        if sum(array) - array[i] - array[j] == 100:
            x, y = i, j
            break

array.pop(x)
array.pop(y - 1) # pop하면 리스트의 길이가 줄어드니 y - 1을 pop한다.

for i in array:
    print(i)