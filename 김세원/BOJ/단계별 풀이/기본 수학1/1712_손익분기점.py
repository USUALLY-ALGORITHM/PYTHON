a,b,c = map(int, input().split())

if b >= c:
    print(-1)
else:
    cnt = (a//(c-b))+1
    print(cnt)
