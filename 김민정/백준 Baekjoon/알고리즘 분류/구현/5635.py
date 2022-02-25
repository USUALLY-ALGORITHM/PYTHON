# 생일 (https://www.acmicpc.net/problem/5635)

N = int(input())

info = []
for i in range(N):
    name, dd, mm, yyyy = input().rstrip().split() # rstrip : 오른쪽 공백 제거
    dd, mm, yy = map(int, (dd, mm, yyyy))
    info.append((yyyy, mm, dd, name))

info.sort()

print(info[-1][3])
print(info[0][3])