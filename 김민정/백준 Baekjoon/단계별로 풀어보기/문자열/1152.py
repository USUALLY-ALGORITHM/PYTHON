# 단어의 개수 (https://www.acmicpc.net/problem/1152)

arr = input()

count = 1
for i in arr:
    if i == ' ':
        count += 1

if arr[0] == ' ':
    count -= 1
if arr[len(arr) - 1] == ' ':
    count -= 1
print(count)

"""
a = input().split()
print(len(a))
"""