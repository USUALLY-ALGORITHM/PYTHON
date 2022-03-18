# 잃어버린 괄호 (https://www.acmicpc.net/problem/1541)

s = input().split('-')

num = 0
for i in s[0].split('+'):
    num += int(i)

for i in s[1:]:
    for j in i.split('+'):
        num -= int(j)

print(num)