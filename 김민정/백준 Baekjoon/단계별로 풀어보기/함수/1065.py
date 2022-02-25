# 한수 (https://www.acmicpc.net/problem/1065)

X = int(input())

count = 0
for i in range(1, X + 1):
    if i < 100:
        count += 1
    else:
        X_str = list(map(int, str(i)))
        if X_str[2] - X_str[1] == X_str[1] - X_str[0]:
            count += 1
print(count)