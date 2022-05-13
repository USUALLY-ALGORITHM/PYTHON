# 수리공 항승 (https://www.acmicpc.net/problem/1449)

N, L = int(input().split())
array = list(map(int, input().split()))

array.sort()

# 테이프를 처음 붙이는 시작 지점
start = array[0]
# 필요한 테이프의 개수
count = 1

# 물이 새는 곳의 위치를 차례대로 받기
for location in array[1:]:
    # 테이프를 붙이는 범위 내에 물이 새는 곳의 위치가 있다면
    if location in range(start, start + L):
        # 기존의 테이프 사용
        continue
    # 기존의 테이프로 붙이지 못한다면
    else:
        # 새 테이프를 사용하고 테이프 개수 추가
        start = location
        count += 1

# 필요한 테이프의 개수 출력
print(count)

# https://data-flower.tistory.com/53
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=pjok1122&logNo=221652284982

"""
N,L = map(int, input().split())

location = list(map(int,input().split()))
location.sort()

start = 0
cnt = 0
for loc in location:
    if start < loc:
        # start + L - 1 까지는 자동으로 수리됨.
        start = loc + L - 1
        cnt += 1

print(cnt)
"""