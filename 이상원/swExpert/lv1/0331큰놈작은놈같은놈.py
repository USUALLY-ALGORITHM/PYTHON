answer = []
n = int(input())
for item in range(n):
    a, b = map(int, input().split())
    if a > b:
        answer.append('>')
    elif a < b:
        answer.append('<')
    else:
        answer.append('=')

for item in range(n):
    print(f'#{item+1} {answer[item]}')
