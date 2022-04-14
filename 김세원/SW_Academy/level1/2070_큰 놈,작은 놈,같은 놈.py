n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    if x<y:
        print(f'#{i + 1}', "<")
    elif x==y:
        print(f'#{i + 1}', "=")
    elif x>y:
        print(f'#{i + 1}', ">")
