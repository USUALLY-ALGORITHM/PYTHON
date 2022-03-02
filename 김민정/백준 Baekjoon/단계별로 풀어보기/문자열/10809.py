# 알파벳 찾기 (https://www.acmicpc.net/problem/10809)

S = input()

arr = []
for i in range(97, 123):
    if chr(i) in S:
        arr.append(S.index(chr(i)))
    else:
        arr.append(-1)

for i in arr:
    print(i, end = ' ')

"""
S = str(input())
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(arr)):
    print(S.find(arr[i]), end = " ")
"""
