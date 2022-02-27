# 두 수 비교하기 (https://www.acmicpc.net/problem/1330)

A, B = map(int, input().split())

if A > B:
    print('>')
if A < B:
    print('<')
if A == B:
    print('==')