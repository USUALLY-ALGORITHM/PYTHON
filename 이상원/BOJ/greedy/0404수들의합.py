'''
https://www.acmicpc.net/problem/1789
'''
n = int(input())
answer = 0
nums = 0
for i in range(1, n+1):
    nums += i
    if nums > n:
        answer = i-1
        break
print(answer)
